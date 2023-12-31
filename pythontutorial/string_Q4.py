"""Write a function which accept a string and substring and return the occurrences
count of a substring in a string.
"""


def string(s, ss):
    count = 0
    ssl = len(ss)
    for i in range(len(s)):
        if s[i:i + ssl] == ss:
            count += 1
    return count


print(string("dsdgsvvdshellodgdcydhellohellohellohello", "hello"))
