# Create a new dictionary, where
# "John", "Jane" and "Gerard" are keys and numbers are values.
phone_book = {"John": 123, "Jane": 234, "Gerard": 345}
# print(phone_book)
#
# # Add a new item to the dictionary.
# phone_book["Jill"] = 345
# print(phone_book)
#
# # Remove a key-value pair from phone_book.
# del phone_book["John"]
#
# phone_book["Jared"] = 570
#
# del phone_book["Gerard"]
#
# print(phone_book)
# print(phone_book["Jane"])

for i, j in phone_book.items():
    if j == 234:
        print(i)
        del phone_book[i]
# i = john, j = 123
# i = Jane, j = 234
# Jane
#