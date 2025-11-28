#!/usr/bin/env python3
"""P6.01: File Organizer

Organize files into subdirectories based on their extensions.

Problem:
    Given a dictionary representing files in a directory:
    {filename: content, ...}

    Return a dictionary representing the organized structure:
    {
        "images": {"photo.jpg": "...", "icon.png": "..."},
        "documents": {"report.pdf": "...", "notes.txt": "..."},
        "other": {"readme": "..."}
    }

    Categories:
    - images: .jpg, .jpeg, .png, .gif, .bmp
    - documents: .pdf, .doc, .docx, .txt, .md
    - code: .py, .js, .ts, .java, .cpp, .c, .h
    - data: .json, .csv, .xml, .yaml, .yml
    - other: everything else (including files without extensions)

Example:
    Input: {"photo.jpg": "img", "script.py": "code", "data.csv": "data", "README": "text"}

    Output: {
        "images": {"photo.jpg": "img"},
        "code": {"script.py": "code"},
        "data": {"data.csv": "data"},
        "other": {"README": "text"}
    }

Complexity:
    Time: O(n) where n is number of files
    Space: O(n) for the organized structure
"""

from pathlib import Path


def organize_files(files: dict[str, str]) -> dict[str, dict[str, str]]:
    """Organize files into category subdirectories.

    Args:
        files: Dictionary mapping filename to content

    Returns:
        Nested dictionary with categories as keys
    """
    # TODO - you fill in here.
    return {}


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework.practical_test import run_tests

    exit(run_tests('file_organizer_tests.json', organize_files))
