"""Solution for Reshaping"""
import pandas as pd


def wide_to_long(df: pd.DataFrame, id_col: str, value_vars: list) -> pd.DataFrame:
    return pd.melt(df, id_vars=[id_col], value_vars=value_vars)


def pivot_mean_sales(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(index='product', columns='month', values='sales', aggfunc='mean')
