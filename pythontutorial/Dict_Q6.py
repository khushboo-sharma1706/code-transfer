"""Q6: Write a Python program to create a dictionary of keys x, y, and z where each key has
as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key
from the dictionary"""

dict1 = dict()
dict1['x'] = list(range(11,21))
dict1['y'] = list(range(21,31))
dict1['z'] = list(range(31,41))

for v in dict1.values():
    print(v[4])
"""print(dict1)
print(dict1["x"])
print(dict1["x"][4])"""



