
def frac_weights(d, m=100):
    w = [1]
    for k in range(1, m + 1):
        w.append(-w[-1] * ((d - k + 1) / k))
    return w
