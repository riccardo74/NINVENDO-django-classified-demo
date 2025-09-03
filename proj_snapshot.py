# snapshot_django.py — Create a concise CONTEXT.md of your Django project
# (+ optional Git history), with targeted capture for 'trade' app, messaging,
# and user/profile pieces needed for in-app chat. Tailored for your project
# where the marketplace app is named 'trade' (not 'market').

#python proj_snapshot.py --templates all --templates-max-file-lines 400

#python proj_snapshot.py --templates interesting


from __future__ import annotations
import os, re, sys, argparse, textwrap, pathlib, subprocess, shutil
from typing import List, Literal

# ---------- Configuration ----------

DEFAULT_OUT_DIR = "out"
DEFAULT_MAX_LINES = 4000
DEFAULT_MAX_FILE_LINES = 300
DEFAULT_HTML_MAX_FILE_LINES = 300
DEFAULT_GIT_MAX = 50

EXCLUDE_DIRS = {
    ".git", ".hg", ".svn", ".vscode", ".idea", "__pycache__", ".pytest_cache",
    "node_modules", "static", "media", "dist", "build", ".mypy_cache",
    ".venv", "venv", ".ruff_cache", ".tox", ".coverage", "site-packages",
    "migrations",
}

# Filenames to include ovunque
WANTED_FILENAMES = {
    "manage.py",
    "requirements.txt", "requirements.in", "poetry.lock", "Pipfile", "Pipfile.lock",
    "pyproject.toml",
    "render.yaml", "Procfile", "Dockerfile",
    "README.md", "README.rst", "README.txt",
}

# Suffix “code/text” che vale la pena incorporare
CODE_SUFFIXES = {
    ".py", ".html", ".txt", ".yaml", ".yml", ".toml", ".lock",
    ".js", ".ts", ".css"
}

# File app-level che vogliamo sempre
APP_CODE_FILES = {
    "models.py", "views.py", "urls.py", "forms.py", "admin.py",
    "serializers.py", "apps.py", "signals.py"
}

# App di interesse
PRIMARY_APP_NAMES = {"trade","payments"}  # marketplace app
MSG_APP_NAMES = {"messaging", "chat", "inbox"}
USER_APP_NAMES = {"users", "accounts", "profiles"}

# Parole chiave template (manteniamo, ma ora c'è una modalità "all")
TEMPLATE_KEYWORDS = (
    "login", "password_reset", "registration", "email_sent", "_base",
    "base", "trade", "account", "signup", "logout", "profile",
    "conversation", "message", "chat", "inbox"
)

TemplatesMode = Literal["all", "interesting", "none"]

# ---------- Redaction ----------

REDACTIONS = [
    (re.compile(r"(SECRET_KEY\s*=\s*)([\"'])(?P<val>.+?)(\2)"), r"\1'***REDACTED***'"),
    (re.compile(r"(SOCIAL_AUTH_[A-Z0-9_]+?\s*=\s*)([\"']?)(?P<val>[^\"'\n]+)([\"']?)"), r"\1'***REDACTED***'"),
    (re.compile(r"os\.environ\.get\(\s*([\"'][A-Z0-9_]+[\"'])\s*,\s*([\"'])(?P<val>.+?)(\2)\s*\)"), r"os.environ.get(\1, '***REDACTED***')"),
    (re.compile(r"(DATABASE_URL|EMAIL_URL)\s*=\s*([\"'])(?P<val>.+?)(\2)"), r"\1='***REDACTED***'"),
    (re.compile(r"(?i)(PASSWORD\s*=\s*)([\"'])(?P<val>.+?)(\2)"), r"\1'***REDACTED***'"),
]

def redact(text: str) -> str:
    for pattern, repl in REDACTIONS:
        text = pattern.sub(repl, text)
    return text

# ---------- Helpers ----------

def is_excluded_dir(rel_path: pathlib.Path) -> bool:
    return any(part in EXCLUDE_DIRS for part in rel_path.parts)

def looks_like_project_settings(path: pathlib.Path) -> bool:
    return path.name == "settings.py"

def looks_like_project_urls(path: pathlib.Path) -> bool:
    # keep project urls, but we also include app urls via APP_CODE_FILES
    return path.name == "urls.py" and path.parent.name not in {"tests"}

def is_wanted_misc(path: pathlib.Path) -> bool:
    return path.name in WANTED_FILENAMES

def is_code_file(path: pathlib.Path) -> bool:
    return path.suffix in CODE_SUFFIXES or path.name in WANTED_FILENAMES

def is_app_code_file(path: pathlib.Path) -> bool:
    return path.name in APP_CODE_FILES

def is_template(path: pathlib.Path) -> bool:
    return path.suffix == ".html"

def template_is_interesting(path: pathlib.Path) -> bool:
    """Originale: include se matcha parole chiave o è dentro templates/{trade|messaging|chat|inbox}."""
    if not is_template(path):
        return False
    name = path.name.lower()
    if any(k in name for k in TEMPLATE_KEYWORDS):
        return True
    parts = {p.lower() for p in path.parts}
    if "templates" in parts:
        if {"trade","messaging","chat","inbox"} & parts:
            return True
    return False

def iter_files(root: pathlib.Path):
    for p in root.rglob("*"):
        if p.is_dir():
            continue
        yield p

def collect_template_files(root: pathlib.Path, mode: TemplatesMode) -> List[pathlib.Path]:
    """Raccoglie i template in base alla modalità."""
    if mode == "none":
        return []
    files: List[pathlib.Path] = []
    for p in iter_files(root):
        if not is_template(p):
            continue
        rel = p.relative_to(root)
        if is_excluded_dir(rel.parent):
            continue
        if mode == "all":
            # prendi tutti gli .html sotto qualsiasi cartella 'templates'
            if "templates" in (x.lower() for x in rel.parts):
                files.append(p)
        else:
            # mode == "interesting"
            if template_is_interesting(p):
                files.append(p)
    # de-dup preservando l'ordine
    seen = set()
    ordered = []
    for f in files:
        rp = f.as_posix()
        if rp not in seen:
            seen.add(rp)
            ordered.append(f)
    return ordered

def collect_candidate_files(root: pathlib.Path, templates_mode: TemplatesMode) -> List[pathlib.Path]:
    cand: List[pathlib.Path] = []

    # 1) Generic important files and project-level settings/urls
    for p in iter_files(root):
        rel = p.relative_to(root)
        if is_excluded_dir(rel.parent):
            continue
        if p.name == "manage.py":
            cand.append(p)
            continue
        if is_wanted_misc(p):
            cand.append(p)
            continue
        if looks_like_project_settings(p) or looks_like_project_urls(p):
            cand.append(p)
            continue

    # 2) All app code files everywhere (models/views/urls/forms/etc)
    for p in iter_files(root):
        rel = p.relative_to(root)
        if is_excluded_dir(rel.parent):
            continue
        if is_app_code_file(p):
            cand.append(p)

    # 3) Templates (modalità configurabile)
    cand += collect_template_files(root, templates_mode)

    # 4) PRIORITIZE/INCLUDE: trade, messaging/chat/inbox, users/accounts/profiles (codice + template interessanti)
    important_app_roots = set()
    for app_name in list(PRIMARY_APP_NAMES | MSG_APP_NAMES | USER_APP_NAMES):
        for p in root.rglob(app_name):
            if p.is_dir() and not is_excluded_dir(p.relative_to(root)):
                important_app_roots.add(p)

    for app_root in sorted(important_app_roots):
        for p in app_root.rglob("*"):
            if p.is_dir():
                continue
            rel = p.relative_to(root)
            if is_excluded_dir(rel.parent):
                continue
            if p.name in APP_CODE_FILES or (templates_mode != "none" and template_is_interesting(p)):
                cand.append(p)

    # De-duplicate preserving order
    seen = set()
    ordered = []
    for f in cand:
        rp = f.as_posix()
        if rp not in seen:
            seen.add(rp)
            ordered.append(f)
    return ordered

def make_tree(root: pathlib.Path, max_depth: int = 4) -> str:
    lines = []
    prefix_stack = []
    def walk(dir_path: pathlib.Path, depth: int):
        if depth > max_depth:
            return
        try:
            entries = [e for e in sorted(dir_path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
                       if not (is_excluded_dir(e.relative_to(root)) or e.name.startswith("."))]
        except Exception:
            return
        for i, e in enumerate(entries):
            last = (i == len(entries) - 1)
            branch = "└── " if last else "├── "
            prefix = "".join(prefix_stack) + branch
            if e.is_dir():
                lines.append(f"{prefix}{e.name}/")
                prefix_stack.append("    " if last else "│   ")
                walk(e, depth + 1)
                prefix_stack.pop()
            else:
                lines.append(f"{prefix}{e.name}")
    lines.append(root.resolve().name + "/")
    walk(root, 1)
    return "\n".join(lines)

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
    content = "\n".join(lines)
    if truncated:
        content += f"\n\n<<TRUNCATED: showing first {max_file_lines} lines>>"
    return content

def collect_git_history(root: pathlib.Path, git_max: int) -> str:
    """Return formatted git history or empty string if not available."""
    if shutil.which("git") is None:
        return ""
    try:
        subprocess.check_output(["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"],
                                stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return ""
    cmd = ["git", "-C", str(root), "log",
           f"-n{git_max}",
           "--pretty=format:%h | %ad | %an | %s",
           "--date=short"]
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, encoding="utf-8")
    except subprocess.CalledProcessError:
        return ""
    return out.strip()

# ---------- Main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT_DIR, help="Output directory (default: out)")
    ap.add_argument("--max-lines", type=int, default=DEFAULT_MAX_LINES, help="Max total lines in CONTEXT.md")
    ap.add_argument("--max-file-lines", type=int, default=DEFAULT_MAX_FILE_LINES, help="Max lines per non-HTML file excerpt")
    ap.add_argument("--templates-max-file-lines", type=int, default=DEFAULT_HTML_MAX_FILE_LINES, help="Max lines per HTML template excerpt")
    ap.add_argument("--git-max", type=int, default=DEFAULT_GIT_MAX, help="Max number of git commits to include (0 to disable)")
    ap.add_argument("--templates", choices=["all","interesting","none"], default="interesting",
                    help="How to include templates: 'all' (every .html under templates/), 'interesting' (heuristic), 'none' (skip)")
    args = ap.parse_args()

    root = pathlib.Path(".").resolve()
    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    context_md = out_dir / "CONTEXT.md"

    files = collect_candidate_files(root, args.templates)

    # Pre-split per sezione: templates vs altri
    template_files: List[pathlib.Path] = []
    other_files: List[pathlib.Path] = []
    for p in files:
        if is_template(p):
            # includiamo solo quelli nelle cartelle 'templates' quando in modalità 'all'
            # ma se arrivano qui da 'interesting' li teniamo uguale
            template_files.append(p)
        else:
            other_files.append(p)

    # Assemble document
    doc_parts = []
    doc_parts.append("# Project Snapshot (Django)\n")
    doc_parts.append(f"- Root: `{root}`")
    doc_parts.append(f"- Generated by: `snapshot_django.py`")
    doc_parts.append(f"- Templates mode: `{args.templates}`")
    doc_parts.append("\n---\n")

    # Tree
    doc_parts.append("## Project Tree (compact)\n")
    doc_parts.append("```\n" + make_tree(root, max_depth=4) + "\n```\n")
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
            lang = ""
            if p.suffix == ".py":
                lang = "python"
            elif p.suffix == ".yaml" or p.suffix == ".yml":
                lang = "yaml"
            elif p.suffix == ".js":
                lang = "javascript"
            elif p.suffix == ".ts":
                lang = "typescript"
            elif p.suffix == ".css":
                lang = "css"
            doc_parts.append(f"{fence}{lang}\n{code}\n{fence}\n")

    # Trim to max total lines
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
