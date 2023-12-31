fruits = ['apples', 'bananas', 'peaches', 'grapes']
separator = ' and I like '
joined = separator.join(fruits)
print('I like', joined)


# fruits = ['apples', 'bananas', 'peaches', 'grapes']
# separator = ' and I like '
# joined = separator.join(fruits)
# print('I like', joined)

a = [1,2,3,4,"hjel"]
b = ["abn", "ASdf", "Asdf", "sdf", "asdf"]
print(" < ".join(b))

# y = ""
# for a1 in zip(a,b):
#     print(a1)
#
# print(y)
#
# # print(list(range([1,2,3])))
#
# for i in range(5):
#     print("acv")

for i in enumerate(b[:3]):
    print(i)

z = 0
for i in b[:3]:
    print(": ".join([str(z), i]))
    z += 1

# 0: abn
# 1: ASdf