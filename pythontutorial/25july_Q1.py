# a = ["a", "b", "c", "d"]
# b = [1, 2, 3, 4, 5]
# c = [4, 5, 6]
#
# for x in range(len(a)):
#     print(a[x], b[x])
#
# dict1 = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4
# }

# print(dict1.items())
#
# for k in dict1:
#     print(k)
#
# for k, v in dict1.items():
#     print(k)

# r, f = (1, 3)
#
# print(tuple(zip(a, b, c)))
#
# for d, f, g in zip(a, b, c):
#     print(d, f, g)
#
# arr1 = [300, 400, 100, 1, 40, -1, -100, 0]
# print(min(arr1))
# print(max(arr1))
# print(sum(arr1) / len(arr1))

"""fruit_list = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruit_list = []

for fruit in fruit_list:
    if "a" in fruit:
        new_fruit_list.append(fruit)
print(new_fruit_list)

print([fruit for fruit in fruit_list if "a" in fruit])

# [expression for item in iterable if condition == True]

print([fruit + " good" for fruit in fruit_list if "a" in fruit])

a = "gauri"
b = ["g", "a", "u", "r", "i"]

print([a[i] for i in range(len(a)) if a[i] != "a"])
print([ch for ch in a])

d = [[i * m for i in range(3)] for m in range(10)]
print([(min(i), max(i)) for i in d])
print(sum([sum(i) for i in d]))
print([i for i in range(21) if i % 2 == 0])"""
# [[0, 0, 0], [0, 1, 2], [0, 2, 4], [0, 3, 6], [0, 4, 8], [0, 5, 10], [0, 6, 12], [0, 7, 14], [0, 8, 16], [0, 9, 18]]

list_1 = list(range(1, 21))
print(list_1)
list_1.extend(range(1,11))
print(list_1)

list_2 = (list(set(list_1)))
print(list_2)
print(sum(list_2))
print(min(list_2))
print(max(list_2))
print(sum(list_2)/len(list_2))

print([[i*j for i in range(3)] for j in range(5)])
print([i for i in range(1,11) if i%2 != 0])