from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from .frac_weights import frac_weights
from .find_truncation import find_truncation
from .apply_weights import apply_weights


class FracDiff(BaseEstimator, TransformerMixin):
    def __init__(self, order: float = 1.0, weights: list = None,
                 truncation: int = None, tau: float = 1e-5, mmax: int = 20000,
                 dtype=None):
        # error checking
        if order is None:
            raise Exception('order must be a real positive number d>0')
        # store attributes
        self.order = order
        self.weights = weights
        self.truncation = truncation
        self.tau = tau
        self.mmax = mmax
        self.dtype = dtype

    def fit(self, X: np.ndarray, y=None):
        # determine weights
        if self.weights is None:
            if isinstance(self.truncation, int):
                self.weights = frac_weights(self.order, self.truncation)
            else:  # 'find' or None
                _, self.weights = find_truncation(
                    self.order, tau=self.tau, mmax=self.mmax)
        self.weights = np.array(self.weights)

        # enforce float data type
        if self.dtype is None:
            self.dtype = X[0].dtype if isinstance(X[0], float) else float

        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        # multiply weights with lagged feature x
        if len(X.shape) == 1:
            Z = apply_weights(X.astype(self.dtype), self.weights)
        else:
            Z = np.empty(shape=X.shape)
            for j in range(X.shape[1]):
                Z[:, j] = apply_weights(
                    X[:, j].astype(self.dtype), self.weights)
        return Z

    # def inverse_transform(self, Z: np.ndarray) -> np.ndarray:
    #    pass  # return X
