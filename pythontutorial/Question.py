"""for x in range(0, 20, 2):
    print(x)

for x in range(18, -1, -2):
    print(x)
"""


def fact(n):
    r = 1
    for m in range(1, n + 1):
        r *= m
    return r
print(fact(6))


