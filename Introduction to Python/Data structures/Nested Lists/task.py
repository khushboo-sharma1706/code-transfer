my_list = [[1, [2, 3]], [4, 5, 6], [7, 8, 9], 10]

print(my_list[2][2])
print(my_list[3])

print(f"I have found {my_list[0][1][1]}")

my_list[0][1][1] = [3]
print(my_list)

