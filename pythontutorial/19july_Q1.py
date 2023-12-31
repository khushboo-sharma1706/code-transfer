"""Q1: Write a function that prints each item and its corresponding type from the following list.
Sample List: datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
"""

def q(l):
    l2 = []
    for i in l:
        a = type(i)
        l2.append(a)
    return l2

print(q([1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]))


"""def q(l):
    d = {}
    for i in l:
        a = type(i)
        d[i] = a
    return d


print(q([1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]))
"""