import numba


@numba.jit(nopython=True)
def find_truncation(d: float,
                    tau: float = 1e-5,
                    mmax: int = 20000) -> (int, list):
    w = [1]
    for k in range(1, mmax + 1):
        wk = -w[-1] * ((d - k + 1) / k)
        if abs(wk) < tau:
            break
        w.append(wk)
    return k - 1, w
