#!/usr/bin/env python3
"""P5.01: SQL Aggregation Query

Write SQL queries to aggregate data from an in-memory SQLite database.

Problem:
    Given a SQLite connection with a 'sales' table:
    - id (INTEGER)
    - product (TEXT)
    - category (TEXT)
    - quantity (INTEGER)
    - price (REAL)
    - sale_date (TEXT)

    Write a query that returns the total revenue per category,
    sorted by revenue descending.

    Return a list of tuples: [(category, total_revenue), ...]

Example:
    Sales table:
        | product | category    | quantity | price |
        |---------|-------------|----------|-------|
        | Widget  | Electronics | 10       | 5.00  |
        | Gadget  | Electronics | 5        | 10.00 |
        | Chair   | Furniture   | 2        | 50.00 |

    Result: [("Electronics", 100.0), ("Furniture", 100.0)]

Complexity:
    Time: O(n log n) for sorting
    Space: O(c) where c is number of categories
"""

import sqlite3
from pathlib import Path


def get_revenue_by_category(conn: sqlite3.Connection) -> list[tuple[str, float]]:
    """Query total revenue per category from sales table.

    Args:
        conn: SQLite database connection with 'sales' table

    Returns:
        List of (category, total_revenue) tuples, sorted by revenue desc
    """
    # TODO - you fill in here.
    # Hint: Use SQL with GROUP BY and ORDER BY
    return []


if __name__ == '__main__':
    import sys
    import json
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework.practical_test import load_test_cases

    def run_sql_tests():
        """Custom test runner for SQL tests."""
        test_cases = load_test_cases('sql_aggregation_tests.json')
        passed = 0
        failed = 0

        for i, test_case in enumerate(test_cases, 1):
            setup_sql = test_case['input']['setup_sql']
            insert_data = test_case['input']['insert_data']
            expected = [tuple(row) for row in test_case['expected']]
            description = test_case.get('description', f'Test case {i}')

            # Create in-memory database
            conn = sqlite3.connect(':memory:')
            cursor = conn.cursor()

            try:
                # Setup table
                cursor.execute(setup_sql)

                # Insert test data
                for row in insert_data:
                    cursor.execute(
                        "INSERT INTO sales (product, category, quantity, price, sale_date) VALUES (?, ?, ?, ?, ?)",
                        row
                    )
                conn.commit()

                result = get_revenue_by_category(conn)

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
            finally:
                conn.close()

        print(f"\n{passed}/{passed + failed} tests passed")
        return 0 if failed == 0 else 1

    exit(run_sql_tests())
