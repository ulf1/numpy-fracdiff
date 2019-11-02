
def find_truncation(d, tau=1e-5, mmax=20000):
    w = [1]
    for k in range(1, mmax + 1):
        wk = -w[-1] * ((d - k + 1) / k)
        if abs(wk) < tau:
            break
        w.append(wk)
    return k-1, w
