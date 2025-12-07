#!/usr/bin/env python3
"""M4.02: Custom sklearn Transformer

Implement a custom sklearn transformer following the fit/transform pattern.

Problem:
    Create custom transformers that integrate with sklearn pipelines:
    1. Inherit from BaseEstimator and TransformerMixin
    2. Implement fit(X, y=None) and transform(X)
    3. Return self from fit()

    Example transformers to implement:
    - OutlierClipper: Clip values to percentile range
    - LogTransformer: Apply log1p to specified columns

Functions to implement:
    1. OutlierClipper class
       - fit: Compute percentile bounds
       - transform: Clip values to bounds

    2. LogTransformer class
       - fit: No-op (stateless)
       - transform: Apply np.log1p to columns

Example:
    clipper = OutlierClipper(lower=5, upper=95)
    clipper.fit(X_train)
    X_clipped = clipper.transform(X_test)

    # Use in pipeline
    pipeline = Pipeline([
        ('clip', OutlierClipper()),
        ('log', LogTransformer(columns=['income'])),
        ('scale', StandardScaler())
    ])

Edge Cases:
    - Empty fit data
    - Negative values for log transform
    - Columns not in transform data

Complexity:
    Time: O(n) for fit and transform
    Space: O(d) for storing bounds
"""

import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.base import BaseEstimator, TransformerMixin


class OutlierClipper(BaseEstimator, TransformerMixin):
    """Clip outliers to percentile bounds.

    Args:
        lower_percentile: Lower bound percentile (default 5)
        upper_percentile: Upper bound percentile (default 95)
    """

    def __init__(self, lower_percentile: float = 5, upper_percentile: float = 95):
        self.lower_percentile = lower_percentile
        self.upper_percentile = upper_percentile
        self.lower_bounds_ = None
        self.upper_bounds_ = None

    def fit(self, X, y=None):
        """Compute percentile bounds from training data.

        Args:
            X: Training data (array or DataFrame)
            y: Ignored

        Returns:
            self
        """
        # TODO - you fill in here.
        return self

    def transform(self, X):
        """Clip values to computed bounds.

        Args:
            X: Data to transform

        Returns:
            Clipped data
        """
        # TODO - you fill in here.
        return X


class LogTransformer(BaseEstimator, TransformerMixin):
    """Apply log1p transform to specified columns.

    Args:
        columns: List of column names/indices to transform.
                 If None, transform all columns.
    """

    def __init__(self, columns=None):
        self.columns = columns

    def fit(self, X, y=None):
        """No-op fit (stateless transformer).

        Returns:
            self
        """
        # TODO - you fill in here.
        return self

    def transform(self, X):
        """Apply log1p to specified columns.

        Args:
            X: Data to transform

        Returns:
            Transformed data
        """
        # TODO - you fill in here.
        return X


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(X_train, X_test, transformer_type, **kwargs):
        X_train = np.array(X_train)
        X_test = np.array(X_test)

        if transformer_type == 'clipper':
            transformer = OutlierClipper(**kwargs)
        else:
            transformer = LogTransformer(**kwargs)

        transformer.fit(X_train)
        result = transformer.transform(X_test)
        return np.round(result, 4).tolist()

    exit(run_tests('custom_transformer_tests.json', test_wrapper))
