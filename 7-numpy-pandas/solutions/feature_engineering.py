"""Solution for Feature Engineering"""
import pandas as pd
import numpy as np


def engineer_transaction_features(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result['timestamp'] = pd.to_datetime(result['timestamp'])

    # Day of week
    result['day_of_week'] = result['timestamp'].dt.dayofweek

    # Time since last transaction per user
    result = result.sort_values(['user_id', 'timestamp'])
    result['time_since_last'] = result.groupby('user_id')['timestamp'].diff().dt.total_seconds()

    # Transaction count in past 7 days per user
    # This is more complex - using a rolling window on sorted data
    result['txn_count_7d'] = result.groupby('user_id').apply(
        lambda g: g.set_index('timestamp').rolling('7D').count()['amount']
    ).reset_index(level=0, drop=True)

    return result
