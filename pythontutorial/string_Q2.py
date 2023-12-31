"""Write a Python program to add 'ing' at the end of a given string (length should be
 at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of
the given string is less than 3, leave it unchanged."""

def string(n):
    if len(n) < 3:
        return n
    elif n[-3:] == "ing":
        return n[:-3]+"ly"
    else:
        return n+"ing"


print(string("opening"))
print(string("Open"))
print(string("Ma"))