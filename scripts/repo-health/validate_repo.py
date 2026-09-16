import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

# Config
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = REPO_ROOT / "docs"
IGNORE_DIRS = {".git", "node_modules", "__pycache__", "assets", "dist", "build"}

# Lightweight, deterministic heuristics for common secret formats.
# This is a baseline guard, not a replacement for GitHub Secret Scanning.
SECRET_PATTERNS = [
    ("private key", re.compile(r"-----BEGIN\s+[A-Z\s]+PRIVATE\s+KEY-----", re.IGNORECASE)),
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("GitHub token", re.compile(r"(?:gh[pousr]_[A-Za-z0-9_]{30,}|github_pat_[A-Za-z0-9_]{40,})")),
    ("OpenAI-style API key", re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z_-]{35}")),
    ("JWT", re.compile(r"ey[a-zA-Z0-9_-]{2,}\.[a-zA-Z0-9_-]{2,}\.[a-zA-Z0-9_-]+")),
]

JWT_SENSITIVE_SUFFIXES = {".env", ".json", ".yml", ".yaml"}


def check_secrets(filepath: Path):
    """Check a UTF-8 text file for obvious secret patterns."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None

    for name, pattern in SECRET_PATTERNS:
        if name == "JWT" and filepath.suffix.lower() not in JWT_SENSITIVE_SUFFIXES and filepath.name != ".env":
            continue
        if pattern.search(content):
            return f"Potential {name} found in {filepath.relative_to(REPO_ROOT)}"
    return None


def check_markdown_links(filepath: Path):
    """Check relative/local Markdown links and reject paths escaping the repository."""
    errors = []
    try:
        content = filepath.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return errors

    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    for _text, raw_link in links:
        link = raw_link.strip().strip("<>")
        if link.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            continue

        link_path = unquote(link.split("#", 1)[0].split("?", 1)[0])
        if not link_path:
            continue

        if link_path.startswith("/"):
            target_path = (REPO_ROOT / link_path.lstrip("/")).resolve()
        else:
            target_path = (filepath.parent / link_path).resolve()

        if not target_path.is_relative_to(REPO_ROOT):
            errors.append(
                f"Repository-escaping link in {filepath.relative_to(REPO_ROOT)}: '{raw_link}'"
            )
            continue

        if not target_path.exists():
            errors.append(f"Broken link in {filepath.relative_to(REPO_ROOT)}: '{raw_link}'")

    return errors


def check_frontmatter(filepath: Path):
    """Check required metadata on approved/frozen docs that already use YAML frontmatter."""
    if not filepath.is_relative_to(DOCS_DIR):
        return []

    try:
        content = filepath.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []

    if not content.startswith("---"):
        return []

    end_idx = content.find("---", 3)
    if end_idx == -1:
        return [f"Unclosed frontmatter in {filepath.relative_to(REPO_ROOT)}"]

    frontmatter = content[3:end_idx]
    normalized = frontmatter.lower()
    if "status: approved" in normalized or "status: frozen" in normalized:
        required_fields = ["owner:", "updated:", "authority:"]
        missing = [field for field in required_fields if field not in normalized]
        if missing:
            return [
                f"Missing required frontmatter fields {missing} in canonical doc: "
                f"{filepath.relative_to(REPO_ROOT)}"
            ]
    return []


def main():
    print("Running Repository Health Checks...")
    errors = []

    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            filepath = Path(root) / file

            secret_err = check_secrets(filepath)
            if secret_err:
                errors.append(secret_err)

            if filepath.suffix.lower() == ".md":
                errors.extend(check_markdown_links(filepath))
                errors.extend(check_frontmatter(filepath))

    if errors:
        print("\nRepository Health Checks Failed:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print("\nAll Repository Health Checks Passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
