#!/usr/bin/env python3
"""P4.01: API Pagination Handler

Implement a function that fetches all pages from a paginated API response.

Problem:
    Given an initial API response dict and a fetch function, collect all items
    across all pages. The API response format is:
    {
        "items": [...],
        "next_page": "url" or null
    }

    The fetch function simulates API calls: fetch(url) -> response dict

Example:
    Page 1: {"items": [1, 2], "next_page": "page2"}
    Page 2: {"items": [3, 4], "next_page": "page3"}
    Page 3: {"items": [5], "next_page": null}

    Result: [1, 2, 3, 4, 5]

Complexity:
    Time: O(p) where p is number of pages
    Space: O(n) where n is total number of items
"""

from pathlib import Path
from typing import Callable


def fetch_all_pages(
    initial_response: dict,
    fetch_func: Callable[[str], dict]
) -> list:
    """Fetch all items from a paginated API.

    Args:
        initial_response: The first page response
        fetch_func: Function to fetch subsequent pages by URL

    Returns:
        List of all items across all pages
    """
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework.practical_test import run_tests, load_test_cases

    def run_pagination_tests():
        """Custom test runner for pagination tests."""
        test_cases = load_test_cases('api_pagination_tests.json')
        passed = 0
        failed = 0

        for i, test_case in enumerate(test_cases, 1):
            pages = test_case['input']['pages']
            expected = test_case['expected']
            description = test_case.get('description', f'Test case {i}')

            # Build fetch function from pages data
            def make_fetch(pages_data):
                def fetch(url):
                    return pages_data.get(url, {"items": [], "next_page": None})
                return fetch

            fetch_func = make_fetch(pages)
            initial = pages.get('page1', {"items": [], "next_page": None})

            try:
                result = fetch_all_pages(initial, fetch_func)
                if result == expected:
                    print(f"✓ {description}")
                    passed += 1
                else:
                    print(f"✗ {description}")
                    print(f"  Expected: {expected}")
                    print(f"  Got: {result}")
                    failed += 1
            except Exception as e:
                print(f"✗ {description}")
                print(f"  Error: {type(e).__name__}: {e}")
                failed += 1

        print(f"\n{passed}/{passed + failed} tests passed")
        return 0 if failed == 0 else 1

    exit(run_pagination_tests())
