phone_book = {"John": 123, "Jane": 234, "Gerard": 345}  # Create a new dictionary
print(phone_book.keys())

# Add new item to the dictionary.
phone_book["Jill"] = 456

print(phone_book.keys())

print(phone_book.values())

# "a": 1
# "b": 2
# 3: 3
# "d": 4

test_dict = {
    "a": 1, "b": 2, 3: 3
}
a = test_dict.items()
b = list(test_dict.items())

print(a)
print(b)

print("------")
test_dict["4"] = 4
print(a)
print(b)

for k, v in b:
    if v == 2:
        del test_dict[k]
print(test_dict)