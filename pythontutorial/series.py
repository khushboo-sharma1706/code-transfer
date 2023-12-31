import math
def series(n):
    r = 0
    for m in range(1, n + 1):
        print("m: ", m)
        r_sub = 0
        for x in range(0,m):
            r_sub += (n*math.pow(10,x))
        r += r_sub
        print("adding :", r_sub)
    return r

print("Sum of series :",series(7))