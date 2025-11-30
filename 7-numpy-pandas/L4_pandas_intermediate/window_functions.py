"""
Window Functions

Problem P2.06 - P2.07
"""
import pandas as pd


def rolling_average_7day(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    """
    P2.06: Compute a 7-day rolling average of a column.

    Assumes df is sorted by date. Use min_periods=1 to handle
    the first few rows.

    Args:
        df: DataFrame with a value column (assumed sorted by date)
        value_col: Column to compute rolling average on

    Returns:
        pd.DataFrame: Original DataFrame with new '{value_col}_rolling_7d' column
    """
    # TODO - you fill in here (return a copy)
    pass


def cumulative_sum_per_group(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """
    P2.07: Compute cumulative sum of a value column within each group.

    Example: Cumulative sales per customer over time.

    Args:
        df: DataFrame (assumed sorted by date within each group)
        group_col: Column to group by
        value_col: Column to compute cumsum on

    Returns:
        pd.DataFrame: Original DataFrame with new '{value_col}_cumsum' column
    """
    # TODO - you fill in here (return a copy)
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test P2.06
    df = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=10),
        'price': [10, 12, 11, 13, 15, 14, 16, 18, 17, 19]
    })
    result = rolling_average_7day(df, 'price')
    assert result is not None, "P2.06: Function returned None"
    assert 'price_rolling_7d' in result.columns, "P2.06: Missing rolling column"
    # Day 7 (index 6): mean of [10,12,11,13,15,14,16] = 91/7 = 13
    assert abs(result['price_rolling_7d'].iloc[6] - 13) < 0.01, "P2.06: Wrong rolling value"
    print("P2.06 rolling_average_7day: PASSED")

    # Test P2.07
    df = pd.DataFrame({
        'customer': ['A', 'A', 'A', 'B', 'B'],
        'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-01', '2024-01-02'],
        'sales': [100, 150, 200, 50, 75]
    })
    result = cumulative_sum_per_group(df, 'customer', 'sales')
    assert result is not None, "P2.07: Function returned None"
    assert 'sales_cumsum' in result.columns, "P2.07: Missing cumsum column"
    # A: 100, 250, 450
    # B: 50, 125
    a_cumsum = result[result['customer'] == 'A']['sales_cumsum'].tolist()
    assert a_cumsum == [100, 250, 450], f"P2.07: A cumsum should be [100,250,450], got {a_cumsum}"
    print("P2.07 cumulative_sum_per_group: PASSED")

    print("\nAll window function tests passed!")
