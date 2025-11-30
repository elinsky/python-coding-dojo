"""Solution for GroupBy & Aggregation"""
import pandas as pd


def total_and_mean_per_group(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('product', as_index=False).agg(
        total_sales=('sales', 'sum'),
        mean_sales=('sales', 'mean')
    )


def rank_within_group(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    result = df.copy()
    result['rank'] = result.groupby(group_col)[value_col].rank(ascending=False, method='min')
    return result
