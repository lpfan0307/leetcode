def sqrt(x):
    if x == 0:
        return 0
    res = 1
    while abs(res * res - x) > 0.01:
        res = 0.5 * (res + 1.*x/res)
    return res

print(sqrt(16))