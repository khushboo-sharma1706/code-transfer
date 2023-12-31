"""Q4: Write a Python program to remove all duplicates from a given list of strings and
return a list of unique strings."""

lst = ["1", "2", "3", "4", "2", "3", "4", "5", "7"]
Ul = []
for i in lst:
    if i not in Ul:
        Ul.append(i)
    else:
        pass
print(Ul)


