from .find_truncation import find_truncation
from .frac_weights import frac_weights
from .apply_weights import apply_weights
import numpy as np


def fracdiff(X: np.ndarray, order: float = None, weights: list = None,
             truncation: int = None, tau: float = 1e-5, mmax: int = 20000,
             dtype=None) -> np.ndarray:
    # determine weights
    if weights is None:
        d = order if order else 0  # Default value, no differentiation
        if isinstance(truncation, int):
            weights = frac_weights(d, truncation)
        else:  # 'find' or None
            _, weights = find_truncation(d, tau=tau, mmax=mmax)

    # enforce float data type
    if dtype is None:
        dtype = X[0].dtype if isinstance(X[0], float) else float

    # multiply weights with lagged feature x
    weights = np.array(weights)
    if len(X.shape) == 1:
        Z = apply_weights(X.astype(dtype), weights)
    else:
        Z = np.empty(shape=X.shape)
        for j in range(X.shape[1]):
            Z[:, j] = apply_weights(X[:, j].astype(dtype), weights)

    # done
    return Z
