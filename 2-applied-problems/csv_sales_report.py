#!/usr/bin/env python3
"""P1.01: CSV Sales Report

Parse a CSV file containing sales data and compute aggregated statistics.

Problem:
    Given a CSV file with columns: date, product, quantity, unit_price
    Return a dictionary with:
    - total_revenue: sum of (quantity * unit_price) for all rows
    - products: dict mapping product name to total quantity sold
    - top_product: name of the product with highest total revenue

Example:
    Input CSV:
        date,product,quantity,unit_price
        2024-01-01,Widget,10,5.00
        2024-01-01,Gadget,5,10.00
        2024-01-02,Widget,3,5.00

    Output:
        {
            "total_revenue": 115.0,
            "products": {"Widget": 13, "Gadget": 5},
            "top_product": "Widget"
        }

Complexity:
    Time: O(n) where n is number of rows
    Space: O(p) where p is number of unique products
"""

import csv
from pathlib import Path


def analyze_sales(csv_path: str) -> dict:
    """Analyze sales data from a CSV file.

    Args:
        csv_path: Path to the CSV file

    Returns:
        Dictionary with total_revenue, products dict, and top_product
    """
    # TODO - you fill in here.
    return {}


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from test_framework.practical_test import run_tests, get_test_data_path

    def test_wrapper(csv_filename: str) -> dict:
        return analyze_sales(str(get_test_data_path(csv_filename)))

    exit(run_tests('csv_sales_report_tests.json', test_wrapper))
