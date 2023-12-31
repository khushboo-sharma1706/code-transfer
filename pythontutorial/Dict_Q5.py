"""Write a function to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Return Output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}"""

def add(d1,d2):
    for k in d1:
        if k in d2:
            d2[k] += d1[k]
        else:
            d2[k] = d1[k]

    return d2
print(add({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400}))