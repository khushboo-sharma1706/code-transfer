"""Write a function to take a tuple and return a dictionary with count of each value.
Input: (2, 4, 5, 6, 2, 3, 4, 4, 7)
Output: {2: 2, 3: 1, 4: 3, 5: 1, 6: 1, 7: 1}"""

d = {}


def Q(t):
    for i in t:
        if i not in d:
            d[i] = 0
        d[i] += 1
    return d


print(Q((2, 4, 5, 6, 2, 3, 4, 4, 7)))
