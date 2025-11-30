"""
Joining / Merging

Problem P2.03
"""
import pandas as pd
import numpy as np


def merge_with_missing_handling(df1: pd.DataFrame, df2: pd.DataFrame, key: str) -> pd.DataFrame:
    """
    P2.03: Merge two DataFrames on a key with a left join.

    Fill any missing values in numeric columns with 0.

    Args:
        df1: Left DataFrame
        df2: Right DataFrame
        key: Column name to join on

    Returns:
        pd.DataFrame: Merged DataFrame with missing numerics filled with 0
    """
    # TODO - you fill in here
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test P2.03
    df1 = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['A', 'B', 'C', 'D']
    })
    df2 = pd.DataFrame({
        'id': [1, 2, 5],
        'value': [100, 200, 500]
    })
    result = merge_with_missing_handling(df1, df2, 'id')
    assert result is not None, "P2.03: Function returned None"
    assert len(result) == 4, f"P2.03: Expected 4 rows (left join), got {len(result)}"
    # Check that missing values are filled with 0
    row_c = result[result['name'] == 'C']['value'].iloc[0]
    assert row_c == 0, f"P2.03: Missing value should be 0, got {row_c}"
    row_a = result[result['name'] == 'A']['value'].iloc[0]
    assert row_a == 100, f"P2.03: A's value should be 100, got {row_a}"
    print("P2.03 merge_with_missing_handling: PASSED")

    print("\nAll merging tests passed!")
