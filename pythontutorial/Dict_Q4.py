"""Write a function which accept dictionary and value and return list of keys matching that value
Dict: {"a": 1, "b": 2, "c": 1, "d": 1}
Value: 1
Return Output: ["a", "c", "d"]"""

def dict_v(d,l):
    list1 = []
    for k,v in d.items():
        if v == l:
            list1.append(k)
    return list1


    pass
print(dict_v({"a": 1, "b": 2, "c": 1, "d": 1},1))
