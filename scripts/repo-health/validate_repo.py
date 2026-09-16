import os
import re
import sys
from pathlib import Path

# Config
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = REPO_ROOT / 'docs'
IGNORE_DIRS = {'.git', '.github', 'node_modules', '__pycache__', 'assets', 'dist', 'build'}

# Regex for common secrets (very basic heuristic)
SECRET_PATTERNS = [
    re.compile(r'-----BEGIN\s+[A-Z\s]+PRIVATE\s+KEY-----', re.IGNORECASE),
    re.compile(r'AKIA[0-9A-Z]{16}'), # AWS Access Key ID
    re.compile(r'ghp_[a-zA-Z0-9]{36}'), # GitHub PAT
    re.compile(r'ey[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9\-_]+'), # Basic JWT structural check (can be noisy, but good for baseline)
]

def check_secrets(filepath):
    """Check a file for obvious secret patterns."""
    try:
        content = filepath.read_text(encoding='utf-8')
        for idx, pattern in enumerate(SECRET_PATTERNS):
            if pattern.search(content):
                # We skip JWT for general files as it is very noisy, but checking others
                if idx == 3 and not filepath.name.endswith(('.env', '.json', '.yml', '.yaml')):
                    continue
                return f"Potential secret found in {filepath.relative_to(REPO_ROOT)}"
    except UnicodeDecodeError:
        pass # Ignore binary files
    return None

def check_markdown_links(filepath, all_md_files):
    """Check for broken internal markdown links."""
    errors = []
    try:
        content = filepath.read_text(encoding='utf-8')
        # Simple markdown link regex [text](link)
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for text, link in links:
            # Ignore external links and anchors
            if link.startswith(('http://', 'https://', 'mailto:', '#')):
                continue

            # Remove anchors from internal links for file checking
            link_path = link.split('#')[0]
            if not link_path:
                continue

            # Resolve relative link
            target_path = (filepath.parent / link_path).resolve()

            # Check if target exists within repo
            if not target_path.exists():
                errors.append(f"Broken link in {filepath.relative_to(REPO_ROOT)}: '{link}'")
    except UnicodeDecodeError:
        pass
    return errors

def check_frontmatter(filepath):
    """Check if approved docs have required frontmatter."""
    if not filepath.is_relative_to(DOCS_DIR):
        return []

    try:
        content = filepath.read_text(encoding='utf-8')
        if content.startswith('---'):
            end_idx = content.find('---', 3)
            if end_idx != -1:
                frontmatter = content[3:end_idx]
                if 'status: approved' in frontmatter or 'status: frozen' in frontmatter:
                    required_fields = ['owner:', 'updated:', 'authority:']
                    missing = [field for field in required_fields if field not in frontmatter]
                    if missing:
                        return [f"Missing required frontmatter fields {missing} in canonical doc: {filepath.relative_to(REPO_ROOT)}"]
    except UnicodeDecodeError:
        pass
    return []

def main():
    print("Running Repository Health Checks...")
    errors = []
    all_md_files = []

    # First pass: collect all md files
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if file.endswith('.md'):
                all_md_files.append(Path(root) / file)

    # Second pass: check files
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            filepath = Path(root) / file

            # Secret check (all files)
            secret_err = check_secrets(filepath)
            if secret_err:
                errors.append(secret_err)

            if file.endswith('.md'):
                # Link check
                link_errs = check_markdown_links(filepath, all_md_files)
                errors.extend(link_errs)

                # Frontmatter check
                fm_errs = check_frontmatter(filepath)
                errors.extend(fm_errs)

    if errors:
        print("\n❌ Repository Health Checks Failed:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("\n✅ All Repository Health Checks Passed.")
        sys.exit(0)

if __name__ == '__main__':
    main()
