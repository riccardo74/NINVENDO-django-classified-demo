#!/usr/bin/env python3
# proj_snapshot.py — Crea un CONTEXT.md conciso del progetto Django
# con opzionale storia Git, snapshot template, estratti file chiave,
# albero directory e (NOVITÀ) sezione "Recently Changed Files".
#
# Esempi:
#   python proj_snapshot.py --templates interesting
#   python proj_snapshot.py --templates all --templates-max-file-lines 400
#   python proj_snapshot.py --templates all --recent-hours 6
#   python proj_snapshot.py --recent-hours 0  # disattiva "recenti"

from __future__ import annotations
import os
import re
import sys
import argparse
import textwrap
import pathlib
import subprocess
import shutil
from datetime import datetime, timedelta
from typing import List, Literal, Iterable

# ---------- Configurazione di base ----------

DEFAULT_OUT_DIR = "out"
DEFAULT_MAX_LINES = 5000
DEFAULT_MAX_FILE_LINES = 300
DEFAULT_HTML_MAX_FILE_LINES = 300
DEFAULT_GIT_MAX = 50
RECENT_MAX_FILES = 100  # tetto di sicurezza per la sezione "recenti"

# Directory escluse dal walk del progetto
EXCLUDED_DIRS = {
    ".git", ".hg", ".svn", ".idea", ".vscode", "__pycache__",
    "node_modules", "dist", "build", "staticfiles", "media",
    ".venv", "venv", "env", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    ".tox", ".coverage", "coverage", "htmlcov", "site-packages",
    "migrations"  # di solito poco utili nello snapshot
}

# File di app considerati "core"
APP_CODE_FILES = {
    "models.py", "views.py", "urls.py", "forms.py", "admin.py",
    "serializers.py", "apps.py", "signals.py", "permissions.py",
    "tasks.py", "consumers.py", "selectors.py", "services.py"
}

# App "di interesse" (adatta ai tuoi nomi reali)
PRIMARY_APP_NAMES = {"trade", "payments"}
MSG_APP_NAMES = {"messaging", "chat", "inbox"}
USER_APP_NAMES = {"users", "accounts", "profiles"}

TemplatesMode = Literal["all", "interesting", "none"]

# Parole chiave per "templates interesting"
TEMPLATE_KEYWORDS = (
    "login", "password_reset", "registration", "email_sent", "_base", "base",
    "trade", "account", "signup", "logout", "profile",
    "conversation", "message", "chat", "inbox"
)

# ---------- Redaction credenziali & segreti ----------

REDACTIONS = [
    # Django SECRET_KEY = '...'
    (re.compile(r"(SECRET_KEY\s*=\s*)([\"'])(?P<val>.+?)(\2)"), r"\1'***REDACTED***'"),
    # Social auth / variabili "URL"
    (re.compile(r"(SOCIAL_AUTH_[A-Z0-9_]+?\s*=\s*)([\"']?)(?P<val>[^\"'\n]+)([\"']?)"), r"\1'***REDACTED***'"),
    # os.environ.get("FOO", "...") → redazione del default
    (re.compile(r"os\.environ\.get\(\s*([\"'][A-Z0-9_]+[\"'])\s*,\s*([\"'])(?P<val>.+?)(\2)\s*\)"),
     r"os.environ.get(\1, '***REDACTED***')"),
    # DATABASE_URL / EMAIL_URL = '...'
    (re.compile(r"(DATABASE_URL|EMAIL_URL)\s*=\s*([\"'])(?P<val>.+?)(\2)"), r"\1='***REDACTED***'"),
    # qualsiasi PASSWORD = '...'
    (re.compile(r"(?i)(PASSWORD\s*=\s*)([\"'])(?P<val>.+?)(\2)"), r"\1'***REDACTED***'"),
    # Cloudinary URL
    (re.compile(r"(CLOUDINARY_URL\s*=\s*)([\"'])(?P<val>.+?)(\2)"), r"\1'***REDACTED***'"),
]

def redact(text: str) -> str:
    for pat, repl in REDACTIONS:
        text = pat.sub(repl, text)
    return text

# ---------- Utility di identificazione file ----------

def is_excluded_dir(rel_path: pathlib.Path) -> bool:
    """
    Ritorna True se una delle parti della path è in EXCLUDED_DIRS.
    """
    for part in rel_path.parts:
        if part in EXCLUDED_DIRS:
            return True
    return False

def is_template(path: pathlib.Path) -> bool:
    return path.suffix.lower() == ".html"

def is_code_file(path: pathlib.Path) -> bool:
    if path.suffix.lower() in {".py", ".js", ".ts", ".css", ".json", ".yaml", ".yml", ".ini", ".cfg", ".toml", ".env", ".txt", ".md"}:
        return True
    # include anche manage.py, wsgi, asgi, settings
    name = path.name
    if name in {"manage.py", "wsgi.py", "asgi.py"}:
        return True
    return False

def is_app_code_file(path: pathlib.Path) -> bool:
    return path.name in APP_CODE_FILES

def template_is_interesting(path: pathlib.Path) -> bool:
    if not is_template(path):
        return False
    name = path.name.lower()
    if any(k in name for k in TEMPLATE_KEYWORDS):
        return True
    parts = {p.lower() for p in path.parts}
    if "templates" in parts:
        if (PRIMARY_APP_NAMES | MSG_APP_NAMES | USER_APP_NAMES) & parts:
            return True
    return False

# ---------- Walk progetto ----------

def iter_files(root: pathlib.Path) -> Iterable[pathlib.Path]:
    for p in root.rglob("*"):
        if p.is_dir():
            continue
        yield p

def collect_template_files(root: pathlib.Path, mode: TemplatesMode) -> List[pathlib.Path]:
    if mode == "none":
        return []
    files: List[pathlib.Path] = []
    for p in iter_files(root):
        rel = p.relative_to(root)
        if is_excluded_dir(rel.parent):
            continue
        if not is_template(p):
            continue
        if mode == "all":
            files.append(p)
        elif mode == "interesting":
            if template_is_interesting(p):
                files.append(p)
    # Ordina per path
    files.sort(key=lambda x: x.as_posix().lower())
    return files

def collect_candidate_files(root: pathlib.Path, templates_mode: TemplatesMode) -> List[pathlib.Path]:
    """
    Raccoglie:
    - settings.py, urls.py, asgi.py, wsgi.py, manage.py
    - file core delle app (models/views/urls/..)
    - altri file 'interessanti' non-HTML
    NOTA: i template sono gestiti separatamente.
    """
    wanted_names = {"settings.py", "urls.py", "asgi.py", "wsgi.py", "manage.py"}
    files: List[pathlib.Path] = []
    for p in iter_files(root):
        rel = p.relative_to(root)
        if is_excluded_dir(rel.parent):
            continue
        if is_template(p):
            continue  # templates gestiti a parte
        if p.name in wanted_names or is_app_code_file(p) or p.suffix.lower() in {".py", ".ini", ".cfg", ".toml", ".yaml", ".yml"}:
            files.append(p)
    files.sort(key=lambda x: x.as_posix().lower())
    return files

# ---------- Sezione "recenti" ----------

def _best_changed_dt(p: pathlib.Path) -> datetime:
    try:
        st = p.stat()
    except Exception:
        return datetime.fromtimestamp(0)
    ts = getattr(st, "st_mtime", None)
    if ts is None:
        return datetime.fromtimestamp(0)
    return datetime.fromtimestamp(ts)

def collect_recent_files(root: pathlib.Path, hours: int) -> List[pathlib.Path]:
    if not hours or hours <= 0:
        return []
    cutoff = datetime.now() - timedelta(hours=hours)
    recent: List[pathlib.Path] = []
    for p in iter_files(root):
        rel = p.relative_to(root)
        if is_excluded_dir(rel.parent):
            continue
        if not (is_code_file(p) or is_template(p)):
            continue
        if _best_changed_dt(p) >= cutoff:
            recent.append(p)
            if len(recent) >= RECENT_MAX_FILES:
                break
    # Dedup + ordine per path
    seen = set()
    ordered: List[pathlib.Path] = []
    for f in sorted(recent, key=lambda x: x.as_posix().lower()):
        rp = f.as_posix()
        if rp not in seen:
            seen.add(rp)
            ordered.append(f)
    return ordered

# ---------- Lettura file & tree ----------

def read_file_excerpt(path: pathlib.Path, max_file_lines: int) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return f"<<unable to read: {e}>>"
    text = redact(text)
    lines = text.splitlines()
    truncated = False
    if len(lines) > max_file_lines:
        lines = lines[:max_file_lines]
        truncated = True
    out = "\n".join(lines)
    if truncated:
        out += f"\n\n<<TRUNCATED FILE: limited to {max_file_lines} lines>>"
    return out

def build_tree(root: pathlib.Path) -> str:
    """
    Tree semplice tipo:
    project/
    ├── app/
    │   ├── models.py
    │   └── views.py
    └── manage.py
    """
    lines: List[str] = []

    def listdir_filtered(dir_path: pathlib.Path) -> List[pathlib.Path]:
        try:
            entries = [
                e for e in sorted(dir_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
                if not (is_excluded_dir(e.relative_to(root)) or e.name.startswith("."))
            ]
        except Exception:
            return []
        return entries

    def walk(dir_path: pathlib.Path, depth: int, prefix_stack: List[str]):
        entries = listdir_filtered(dir_path)
        for i, e in enumerate(entries):
            last = (i == len(entries) - 1)
            branch = "└── " if last else "├── "
            prefix = "".join(prefix_stack) + branch
            if e.is_dir():
                lines.append(f"{prefix}{e.name}/")
                prefix_stack.append("    " if last else "│   ")
                walk(e, depth + 1, prefix_stack)
                prefix_stack.pop()
            else:
                lines.append(f"{prefix}{e.name}")

    lines.append(root.resolve().name + "/")
    walk(root, 1, [])
    return "\n".join(lines)

# ---------- Storia Git ----------

def collect_git_history(root: pathlib.Path, max_commits: int) -> str:
    git_dir = root / ".git"
    if not git_dir.exists():
        return ""
    try:
        cmd = ["git", "-C", str(root), "log", f"-{max_commits}", "--oneline", "--decorate", "--graph", "--date=short", "--pretty=format:%h %ad %d %s"]
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return out.strip()
    except Exception as e:
        return f"<<Unable to read git history: {e}>>"

# ---------- Main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT_DIR, help="Output directory (default: out)")
    ap.add_argument("--max-lines", type=int, default=DEFAULT_MAX_LINES, help="Max total lines in CONTEXT.md")
    ap.add_argument("--max-file-lines", type=int, default=DEFAULT_MAX_FILE_LINES, help="Max lines per non-HTML file excerpt")
    ap.add_argument("--templates-max-file-lines", type=int, default=DEFAULT_HTML_MAX_FILE_LINES, help="Max lines per HTML template excerpt")
    ap.add_argument("--git-max", type=int, default=DEFAULT_GIT_MAX, help="Max number of git commits to include (0 to disable)")
    ap.add_argument("--templates", choices=["all", "interesting", "none"], default="interesting",
                    help="Which templates to include")
    ap.add_argument("--recent-hours", type=int, default=3,
                    help="Include files changed in the last N hours (0 to disable). Default: 3")
    args = ap.parse_args()

    root = pathlib.Path(".").resolve()
    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    context_md = out_dir / "CONTEXT.md"
    doc_parts: List[str] = []

    # Header
    doc_parts.append("# Project Snapshot\n")
    doc_parts.append(f"_Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")
    doc_parts.append("\n---\n")

    # Tree
    doc_parts.append("## Project Tree (filtered)\n")
    doc_parts.append("```\n" + build_tree(root) + "\n```\n")
    doc_parts.append("\n---\n")

    # Raccolta file
    template_files = collect_template_files(root, args.templates)
    other_files = collect_candidate_files(root, args.templates)

    # Sezione "Recently Changed Files"
    recent_files = collect_recent_files(root, args.recent_hours)
    if recent_files:
        doc_parts.append(f"## Recently Changed Files (last {args.recent_hours}h)\n")
        for p in recent_files:
            rp = p.relative_to(root).as_posix()
            doc_parts.append(f"\n### {rp}\n")
            if is_template(p):
                code = read_file_excerpt(p, args.templates_max_file_lines)
                lang = "html"
            else:
                code = read_file_excerpt(p, args.max_file_lines)
                # mappa estensione per il fenced code block
                ext = p.suffix.lower()
                lang = {
                    ".py": "python",
                    ".yaml": "yaml", ".yml": "yaml",
                    ".js": "javascript",
                    ".ts": "typescript",
                    ".css": "css",
                    ".json": "json",
                    ".toml": "toml",
                    ".ini": "",
                    ".cfg": "",
                    ".md": "md",
                    ".txt": ""
                }.get(ext, "")
            fence = "```"
            doc_parts.append(f"{fence}{lang}\n{code}\n{fence}\n")
        doc_parts.append("\n---\n")

    # Git history
    if args.git_max and args.git_max > 0:
        gh = collect_git_history(root, args.git_max)
        if gh:
            (out_dir / "GIT_HISTORY.txt").write_text(gh + "\n", encoding="utf-8")
            doc_parts.append(f"## Git History (last {args.git_max} commits)\n")
            doc_parts.append("```\n" + gh + "\n```\n")
            doc_parts.append("\n---\n")

    # Templates Snapshot
    if template_files:
        doc_parts.append("## Templates Snapshot\n")
        for p in template_files:
            rp = p.relative_to(root).as_posix()
            doc_parts.append(f"\n### {rp}\n")
            code = read_file_excerpt(p, args.templates_max_file_lines)
            fence = "```"
            lang = "html"
            doc_parts.append(f"{fence}{lang}\n{code}\n{fence}\n")
        doc_parts.append("\n---\n")

    # Key Files (non-HTML)
    if other_files:
        doc_parts.append("## Key Files (redacted excerpts)\n")
        for p in other_files:
            rp = p.relative_to(root).as_posix()
            doc_parts.append(f"\n### {rp}\n")
            code = read_file_excerpt(p, args.max_file_lines)
            fence = "```"
            ext = p.suffix.lower()
            lang = {
                ".py": "python",
                ".yaml": "yaml", ".yml": "yaml",
                ".js": "javascript",
                ".ts": "typescript",
                ".css": "css",
                ".json": "json",
                ".toml": "toml",
                ".ini": "",
                ".cfg": "",
                ".md": "md",
                ".txt": ""
            }.get(ext, "")
            doc_parts.append(f"{fence}{lang}\n{code}\n{fence}\n")
        doc_parts.append("\n---\n")

    # Ricomponi rispettando il limite totale
    full_text = "\n".join(doc_parts)
    lines = full_text.splitlines()
    if len(lines) > args.max_lines:
        lines = lines[:args.max_lines]
        lines.append(f"\n<<TRUNCATED CONTEXT: limited to {args.max_lines} total lines>>")
    final_text = "\n".join(lines)

    context_md.write_text(final_text, encoding="utf-8")
    print(f"Written: {context_md}")
    if (out_dir / "GIT_HISTORY.txt").exists():
        print(f"Written: {out_dir / 'GIT_HISTORY.txt'}")

if __name__ == "__main__":
    main()
