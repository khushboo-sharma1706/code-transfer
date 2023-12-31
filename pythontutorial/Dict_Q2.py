"""Write a function to create a dictionary that contains list of numbers as key
(between 1 and n) and value in form or x*x."""


def test_dict(n):
    dict1 = dict()
    #dict1 = {}
    for x in range(1, n + 1):
        dict1[x] = x * x
    return dict1


print(test_dict(4))
