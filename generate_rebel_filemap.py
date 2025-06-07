import os
import subprocess
from datetime import datetime


EXCLUDE_DIRS = {'.git', '__pycache__', '.pytest_cache'}
EXCLUDE_FILES = {'filemap.txt', 'filemap_log.txt'}


def parse_submodules(directory):
    """Return a list of submodule paths if .gitmodules exists."""
    gitmodules = os.path.join(directory, '.gitmodules')
    if not os.path.exists(gitmodules):
        return None
    paths = []
    try:
        with open(gitmodules, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('path ='):
                    paths.append(line.split('=', 1)[1].strip())
    except Exception:
        pass
    return paths


def build_tree(directory, prefix=""):
    entries = sorted([e for e in os.listdir(directory)
                      if e not in EXCLUDE_FILES and not e.startswith('.')])
    lines = []
    for index, name in enumerate(entries):
        path = os.path.join(directory, name)
        connector = "└── " if index == len(entries) - 1 else "├── "
        lines.append(f"{prefix}{connector}{name}")
        if os.path.isdir(path) and name not in EXCLUDE_DIRS:
            extension = "    " if index == len(entries) - 1 else "│   "
            lines.extend(build_tree(path, prefix + extension))
    return lines


def collect_files(directory):
    file_paths = []
    symlink_exists = False
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
        for file in files:
            if file in EXCLUDE_FILES or file.startswith('.'):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, directory)
            file_paths.append(rel_path)
            if os.path.islink(full_path):
                symlink_exists = True
    return file_paths, symlink_exists


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))

    tree_lines = [f"📁 {os.path.basename(root_dir)}"] + build_tree(root_dir)
    filemap_path = os.path.join(root_dir, 'filemap.txt')
    with open(filemap_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(tree_lines))

    file_paths, symlink_exists = collect_files(root_dir)
    total_files = len(file_paths)

    try:
        commit_id = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'], cwd=root_dir, text=True
        ).strip()
    except Exception:
        commit_id = 'N/A'

    submodules = parse_submodules(root_dir)

    log_lines = [
        f"Date: {datetime.now()}",
        f"Git Commit: {commit_id}",
        f"Total Files: {total_files}"
    ]
    if symlink_exists:
        log_lines.append("Note: Contains symlinks")
    if submodules is None:
        log_lines.append("No submodules detected.")
    else:
        log_lines.append("\nDetected Submodules:")
        log_lines.extend(submodules)

    log_lines.append("\nFiles:")
    log_lines.extend(file_paths)

    log_path = os.path.join(root_dir, 'filemap_log.txt')
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(log_lines))


if __name__ == '__main__':
    main()
