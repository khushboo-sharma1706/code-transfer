# Write a function to return the intersection and union of two sets.

def set1(s1, s2):
    u = s1 | s2 #Union
    i = s1 & s2 #Intersection
    d = s1-s2 #Difference
    sd = s1^s2 #Symmetric difference
    return u, i, d, sd


print(set1({1, 2, 3}, {3, 4, 5}))
