import numba


@numba.jit(nopython=True)
def frac_weights(d: float, m: int = 100) -> list:
    w = [1.0]
    for k in range(1, m + 1):
        w.append(-w[-1] * ((d - k + 1.0) / k))
    return w
