"""
Column Operations

Problem P1.03 - P1.04
"""
import pandas as pd
import numpy as np


def add_discounted_price(df: pd.DataFrame) -> pd.DataFrame:
    """
    P1.03: Add a discounted_price column = price * 0.9

    Args:
        df: DataFrame with a 'price' column

    Returns:
        pd.DataFrame: Same DataFrame with new 'discounted_price' column added
    """
    # TODO - you fill in here (return a copy, don't modify original)
    pass


def fill_missing_with_mean(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    P1.04: Fill missing values in a column with the column's mean.

    Args:
        df: DataFrame with potentially missing values
        column: Name of column to fill

    Returns:
        pd.DataFrame: DataFrame with missing values filled (return a copy)
    """
    # TODO - you fill in here
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test P1.03
    df = pd.DataFrame({'price': [100, 200, 50]})
    result = add_discounted_price(df)
    assert result is not None, "P1.03: Function returned None"
    assert 'discounted_price' in result.columns, "P1.03: Missing 'discounted_price' column"
    expected = [90.0, 180.0, 45.0]
    assert result['discounted_price'].tolist() == expected, f"P1.03: Expected {expected}"
    # Check original not modified
    assert 'discounted_price' not in df.columns, "P1.03: Original DataFrame was modified"
    print("P1.03 add_discounted_price: PASSED")

    # Test P1.04
    df = pd.DataFrame({'value': [10, np.nan, 30, np.nan, 50]})
    result = fill_missing_with_mean(df, 'value')
    assert result is not None, "P1.04: Function returned None"
    assert result['value'].isna().sum() == 0, "P1.04: Still has missing values"
    # Mean of [10, 30, 50] = 30
    assert result['value'].tolist() == [10.0, 30.0, 30.0, 30.0, 50.0], "P1.04: Wrong fill values"
    # Check original not modified
    assert df['value'].isna().sum() == 2, "P1.04: Original DataFrame was modified"
    print("P1.04 fill_missing_with_mean: PASSED")

    print("\nAll column operation tests passed!")
