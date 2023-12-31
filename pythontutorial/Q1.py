"""def fib(n):
    lst = []
    n1 = 0
    n2 = 1

    lst.append(n1)
    lst.append(n2)
    # print(n1,n2, end=" ")
    for x in range(2,n):
        n3 = n1+n2
        n1 = n2
        n2 = n3
        lst.append(n3)
        # print(n3, end=" ")
    return lst
print(fib(10))"""


def fib(n):
    dict1 = {1: 0, 2: 1}
    for x in range(3, n):
        dict1[x] = dict1[x - 1] + dict1[x - 2]

    return dict1


print(fib(8))
