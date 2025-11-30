"""Solution for Column Operations"""
import pandas as pd


def add_discounted_price(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result['discounted_price'] = result['price'] * 0.9
    return result


def fill_missing_with_mean(df: pd.DataFrame, column: str) -> pd.DataFrame:
    result = df.copy()
    result[column] = result[column].fillna(result[column].mean())
    return result
