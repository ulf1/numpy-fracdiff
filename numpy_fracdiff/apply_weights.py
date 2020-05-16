import numpy as np
import numba


@numba.jit(nopython=True)
def apply_weights(x: np.ndarray, w: np.ndarray) -> np.ndarray:
    m = w.shape[0]
    z = w[0] * x
    z[:(m - 1)] = np.nan
    for k in range(1, m):
        z[k:] += w[k] * x[:-k]
    return z
