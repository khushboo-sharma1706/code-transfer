#Write a Python program to iterate over dictionaries using for loops.

test_dict = {"a": 1,"b": 2,"c": 3}
for k, v in test_dict.items():
    print(k, v)

for k in test_dict.keys():
    print(k)

for v in test_dict.values():
    print(v)