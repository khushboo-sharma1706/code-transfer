# 1 + x/1! + x^2/2! + x^3/3! + ... + x^n/n!
import math
def fact(n):
    r = 1
    for m in range(1, n + 1):
        r *= m
    return r
print(fact(3))

def series(x, n):
    r = 0
    for m in range(0, n + 1):
       r += math.pow(x,m) / fact(m)
    return r
print((series(2,4)))

