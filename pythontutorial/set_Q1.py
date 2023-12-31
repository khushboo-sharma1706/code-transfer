"""Write a Python program to convert a list of tuples into a dictionary.
[("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
{'x': [1, 2, 3], 'y': [1, 2], 'z': [1]}
"""

lt = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for i in lt:
    if i[0] not in d:
        d[i[0]] = []
    d[i[0]].append(i[1])
print(d)
