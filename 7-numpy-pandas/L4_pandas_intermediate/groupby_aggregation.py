"""
GroupBy & Aggregation

Problem P2.01 - P2.02
"""
import pandas as pd


def total_and_mean_per_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    P2.01: Compute total and mean sales per product.

    Args:
        df: DataFrame with columns ['product', 'sales']

    Returns:
        pd.DataFrame: Aggregated data with columns ['product', 'total_sales', 'mean_sales']
    """
    # TODO - you fill in here
    pass


def rank_within_group(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """
    P2.02: Add a rank column within each group based on value (descending).

    Example: Rank customers by sales amount within each region.

    Args:
        df: DataFrame
        group_col: Column to group by
        value_col: Column to rank by (higher = better rank)

    Returns:
        pd.DataFrame: Original DataFrame with new 'rank' column added
    """
    # TODO - you fill in here (return a copy)
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test P2.01
    df = pd.DataFrame({
        'product': ['A', 'B', 'A', 'B', 'A'],
        'sales': [100, 200, 50, 150, 75]
    })
    result = total_and_mean_per_group(df)
    assert result is not None, "P2.01: Function returned None"
    assert 'total_sales' in result.columns, "P2.01: Missing 'total_sales' column"
    assert 'mean_sales' in result.columns, "P2.01: Missing 'mean_sales' column"
    a_row = result[result['product'] == 'A'].iloc[0]
    assert a_row['total_sales'] == 225, f"P2.01: A total should be 225, got {a_row['total_sales']}"
    assert a_row['mean_sales'] == 75, f"P2.01: A mean should be 75, got {a_row['mean_sales']}"
    print("P2.01 total_and_mean_per_group: PASSED")

    # Test P2.02
    df = pd.DataFrame({
        'region': ['East', 'East', 'East', 'West', 'West'],
        'customer': ['A', 'B', 'C', 'D', 'E'],
        'sales': [100, 300, 200, 150, 250]
    })
    result = rank_within_group(df, 'region', 'sales')
    assert result is not None, "P2.02: Function returned None"
    assert 'rank' in result.columns, "P2.02: Missing 'rank' column"
    # East: B(300)=1, C(200)=2, A(100)=3
    # West: E(250)=1, D(150)=2
    b_rank = result[result['customer'] == 'B']['rank'].iloc[0]
    assert b_rank == 1, f"P2.02: B should be rank 1, got {b_rank}"
    print("P2.02 rank_within_group: PASSED")

    print("\nAll groupby tests passed!")
