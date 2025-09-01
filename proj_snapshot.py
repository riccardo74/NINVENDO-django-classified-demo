# Update the previously created snapshot_django.py to include Git history (last N commits)
# The script will now accept --git-max N and produce both an embedded section in CONTEXT.md
# and a standalone out/GIT_HISTORY.txt. It will handle missing git or non-repo directories gracefully.



#updated_script = r


"""
snapshot_django.py — Create a concise CONTEXT.md of your Django project
(+ optional Git history) to share with LLMs. It gathers key files, redacts
secrets, and produces a compact project tree + selected code excerpts.

USAGE
-----
    python snapshot_django.py
    # or specify output dir and size limits
    python snapshot_django.py --out out --max-lines 4000 --max-file-lines 300 --git-max 50

RESULT
------
    ./out/CONTEXT.md
    ./out/GIT_HISTORY.txt   (if git is available and repo exists)

WHAT IT COLLECTS
----------------
- manage.py
- requirements(.txt|.in|poetry.lock|pyproject.toml if Python-related)
- runtime/deploy files: render.yaml, Procfile, Dockerfile
- project settings & urls (any */settings.py, */urls.py)
- app-level models.py, views.py, urls.py, forms.py, admin.py, serializers.py
- templates/*.html (selected: auth, base, trade, registration, etc.)
- README.* (root readme if present)
- Git history (last N commits) if available

EXCLUDES
--------
- Secrets redaction via regex (SECRET_KEY, SOCIAL_AUTH_*, DATABASE_URL, EMAIL_*, etc.)
- Folders: .git, .venv/venv, node_modules, __pycache__, static, media, migrations, .pytest_cache,
           .idea, .vscode, build, dist

LIMITS
------
- Max CONTEXT lines: --max-lines (default 4000)
- Max lines per file excerpt: --max-file-lines (default 300)
- Git history length: --git-max (default 50)
"""
from __future__ import annotations
import os, re, sys, argparse, textwrap, pathlib, subprocess, shutil

# ---------- Configuration ----------

DEFAULT_OUT_DIR = "out"
DEFAULT_MAX_LINES = 4000
DEFAULT_MAX_FILE_LINES = 300
DEFAULT_GIT_MAX = 50

EXCLUDE_DIRS = {
    ".git", ".hg", ".svn", ".vscode", ".idea", "__pycache__", ".pytest_cache",
    "node_modules", "static", "media", "dist", "build", ".mypy_cache",
    ".venv", "venv", ".ruff_cache", ".tox", ".coverage", "site-packages",
    "migrations",
}

# File globs to consider (suffix-based checks)
WANTED_SUFFIXES = {
    "manage.py",
    "requirements.txt", "requirements.in", "poetry.lock", "Pipfile", "Pipfile.lock",
    "pyproject.toml",
    "render.yaml", "Procfile", "Dockerfile",
    "README.md", "README.rst", "README.txt",
}

CODE_SUFFIXES = {".py", ".html", ".txt", ".yaml", ".yml", ".toml", ".lock", ""}

TEMPLATE_KEYWORDS = (
    "login", "password_reset", "registration", "email_sent", "_base",
    "base", "trade", "account", "signup", "logout", "profile"
)

APP_CODE_FILES = {"models.py","views.py","urls.py","forms.py","admin.py","serializers.py","apps.py"}

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

def is_excluded_dir(path: pathlib.Path) -> bool:
    return any(part in EXCLUDE_DIRS for part in path.parts)

def looks_like_project_settings(path: pathlib.Path) -> bool:
    return path.name == "settings.py"

def looks_like_project_urls(path: pathlib.Path) -> bool:
    return path.name == "urls.py" and path.parent.name not in {"trade", "tests"}

def is_wanted_template(path: pathlib.Path) -> bool:
    if path.suffix != ".html":
        return False
    name = path.name.lower()
    if any(k in name for k in TEMPLATE_KEYWORDS):
        return True
    if name in {"base.html", "_base.html"}:
        return True
    return False

def is_wanted_misc(path: pathlib.Path) -> bool:
    return path.name in WANTED_SUFFIXES

def is_app_code_file(path: pathlib.Path) -> bool:
    return path.name in APP_CODE_FILES

def iter_files(root: pathlib.Path):
    for p in root.rglob("*"):
        if p.is_dir():
            if is_excluded_dir(p.relative_to(root)):
                pass
            continue
        yield p

def collect_candidate_files(root: pathlib.Path):
    cand = []
    for p in iter_files(root):
        if is_excluded_dir(p.relative_to(root)):
            continue
        if looks_like_project_settings(p) or looks_like_project_urls(p):
            cand.append(p)
        elif is_app_code_file(p):
            cand.append(p)
        elif is_wanted_template(p):
            cand.append(p)
        elif is_wanted_misc(p):
            cand.append(p)
        elif p.name == "manage.py":
            cand.append(p)
    seen = set()
    ordered = []
    for f in cand:
        rp = f.as_posix()
        if rp not in seen:
            seen.add(rp)
            ordered.append(f)
    return ordered

def make_tree(root: pathlib.Path, max_depth: int = 3) -> str:
    lines = []
    prefix_stack = []
    def walk(dir_path: pathlib.Path, depth: int):
        if depth > max_depth:
            return
        entries = [e for e in sorted(dir_path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())) if not (is_excluded_dir(e.relative_to(root)) or e.name.startswith("."))]
        for i, e in enumerate(entries):
            last = (i == len(entries) - 1)
            branch = "└── " if last else "├── "
            prefix = "".join(prefix_stack) + branch
            if e.is_dir():
                lines.append(f"{prefix}{e.name}/")
                prefix_stack.append(("    " if last else "│   "))
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
        # Ensure we're inside a git repo
        subprocess.check_output(["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return ""
    # Pretty log: hash, date, author, subject (no merge bodies)
    cmd = ["git", "-C", str(root), "log", f"-n{git_max}", "--pretty=format:%h | %ad | %an | %s", "--date=short"]
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
    ap.add_argument("--max-file-lines", type=int, default=DEFAULT_MAX_FILE_LINES, help="Max lines per file excerpt")
    ap.add_argument("--git-max", type=int, default=DEFAULT_GIT_MAX, help="Max number of git commits to include (0 to disable)")
    args = ap.parse_args()

    root = pathlib.Path(".").resolve()
    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    context_md = out_dir / "CONTEXT.md"

    files = collect_candidate_files(root)

    # Assemble document
    doc_parts = []

    doc_parts.append("# Project Snapshot (Django)\n")
    doc_parts.append(f"- Root: `{root}`")
    doc_parts.append(f"- Generated by: `snapshot_django.py`")
    doc_parts.append("\n---\n")

    # Tree
    doc_parts.append("## Project Tree (compact)\n")
    doc_parts.append("```\n" + make_tree(root, max_depth=3) + "\n```\n")
    doc_parts.append("\n---\n")

    # Git history
    if args.git_max and args.git_max > 0:
        gh = collect_git_history(root, args.git_max)
        if gh:
            # also write standalone file
            (out_dir / "GIT_HISTORY.txt").write_text(gh + "\n", encoding="utf-8")
            doc_parts.append(f"## Git History (last {args.git_max} commits)\n")
            doc_parts.append("```\n" + gh + "\n```\n")
            doc_parts.append("\n---\n")

    # Files
    doc_parts.append("## Key Files (redacted excerpts)\n")
    for p in files:
        rp = p.relative_to(root).as_posix()
        doc_parts.append(f"\n### {rp}\n")
        code = read_file_excerpt(p, args.max_file_lines)
        fence = "```"
        lang = "python" if p.suffix == ".py" else ("html" if p.suffix == ".html" else ("yaml" if p.suffix in {".yaml", ".yml"} else ""))
        doc_parts.append(f"{fence}{lang}\n{code}\n{fence}\n")

    # Cut down to max total lines
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

