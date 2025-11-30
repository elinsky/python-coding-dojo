"""
Feature Engineering

Problem P2.08
"""
import pandas as pd
import numpy as np


def engineer_transaction_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    P2.08: Given timestamped transactions, create features:
        - day_of_week: 0=Monday, 6=Sunday
        - time_since_last: seconds since user's previous transaction (NaN for first)
        - txn_count_7d: count of transactions by this user in past 7 days (including current)

    Args:
        df: DataFrame with columns ['user_id', 'timestamp', 'amount']
            timestamp should be datetime or convertible to datetime

    Returns:
        pd.DataFrame: Original DataFrame with new feature columns added
    """
    # TODO - you fill in here (return a copy)
    pass


# ============ Tests ============
if __name__ == '__main__':
    df = pd.DataFrame({
        'user_id': ['A', 'A', 'A', 'B', 'B', 'A'],
        'timestamp': pd.to_datetime([
            '2024-01-01 10:00:00',  # Monday
            '2024-01-01 12:00:00',  # Monday, 2 hours later
            '2024-01-08 10:00:00',  # Monday, 7 days later
            '2024-01-02 09:00:00',  # Tuesday
            '2024-01-03 09:00:00',  # Wednesday, 1 day later
            '2024-01-02 14:00:00',  # Tuesday
        ]),
        'amount': [100, 50, 200, 75, 125, 80]
    })

    result = engineer_transaction_features(df)
    assert result is not None, "P2.08: Function returned None"

    # Check day_of_week
    assert 'day_of_week' in result.columns, "P2.08: Missing 'day_of_week'"
    # Jan 1, 2024 is Monday (0)
    assert result.iloc[0]['day_of_week'] == 0, "P2.08: Jan 1 2024 should be Monday (0)"

    # Check time_since_last
    assert 'time_since_last' in result.columns, "P2.08: Missing 'time_since_last'"
    # First transaction per user should be NaN
    first_a = result[(result['user_id'] == 'A')].iloc[0]['time_since_last']
    assert pd.isna(first_a), "P2.08: First transaction should have NaN time_since_last"
    # Second A transaction: 2 hours = 7200 seconds later
    second_a = result[(result['user_id'] == 'A')].iloc[1]['time_since_last']
    assert second_a == 7200, f"P2.08: Expected 7200 seconds, got {second_a}"

    # Check txn_count_7d
    assert 'txn_count_7d' in result.columns, "P2.08: Missing 'txn_count_7d'"

    print("P2.08 engineer_transaction_features: PASSED")

    print("\nAll feature engineering tests passed!")
