"""Solution for M4.02: Custom sklearn Transformer"""
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class OutlierClipper(BaseEstimator, TransformerMixin):
    """Clip outliers to percentile bounds."""

    def __init__(self, lower_percentile: float = 5, upper_percentile: float = 95):
        self.lower_percentile = lower_percentile
        self.upper_percentile = upper_percentile
        self.lower_bounds_ = None
        self.upper_bounds_ = None

    def fit(self, X, y=None):
        """Compute percentile bounds from training data."""
        X = np.asarray(X)
        self.lower_bounds_ = np.percentile(X, self.lower_percentile, axis=0)
        self.upper_bounds_ = np.percentile(X, self.upper_percentile, axis=0)
        return self

    def transform(self, X):
        """Clip values to computed bounds."""
        X = np.asarray(X).copy()
        return np.clip(X, self.lower_bounds_, self.upper_bounds_)


class LogTransformer(BaseEstimator, TransformerMixin):
    """Apply log1p transform to specified columns."""

    def __init__(self, columns=None):
        self.columns = columns

    def fit(self, X, y=None):
        """No-op fit (stateless transformer)."""
        return self

    def transform(self, X):
        """Apply log1p to specified columns."""
        X = np.asarray(X).copy().astype(float)
        if self.columns is None:
            return np.log1p(X)
        else:
            for col in self.columns:
                X[:, col] = np.log1p(X[:, col])
            return X


if __name__ == '__main__':
    import sys
    from pathlib import Path
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
