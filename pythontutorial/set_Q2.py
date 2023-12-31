"""Write a function to remove an empty tuple(s) from a list of tuples.
Input: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']"""


def Q(l):
    r = []
    for i in l:
        print(i)
        if len(i) != 0:
            r.append(i)
            print(r)
    return r

print("Result : ", Q([(), (), ('',), ('a', 'b'), (), (), ('a', 'b', 'c'), ('d')]))

"""def Q(l):
    for i in l[:]: #by this[:] python creates a copy of same
        print(i)
        if len(i) == 0:
            l.remove(i)
    return l

print("Result : ", Q([(), (), ('',), ('a', 'b'), (), (), ('a', 'b', 'c'), ('d')]))"""