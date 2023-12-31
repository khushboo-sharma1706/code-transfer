#Write a function to take a set and value and add that value(/member) to a set.

def Q(s1,v):
    s1.add(v)
    return s1
print(Q({1,4,7},9))