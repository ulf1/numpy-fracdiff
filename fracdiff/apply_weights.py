import numpy as np

def apply_weights(x: np.ndarray, w: list) -> np.ndarray:
    m = len(w)
    z = w[0] * x
    z[:(m - 1)] = np.nan
    for k in range(1, m):
        z[k:] += w[k] * x[:-k]
    return z
