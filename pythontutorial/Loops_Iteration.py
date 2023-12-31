nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found")
        break
    print(num)
print("\n")

for num in nums:
    if num == 3:
        print("Found")
        continue
    print(num)
print("\n")

for num in nums:
    for letter in 'abc':
        print(num, letter)
print("\n")

for i in range(1,11):
    print(i)
print("\n")

x = 0
while x < 10:
    if x == 5:
        break
    print(x, end=" ")
    x += 1
print("\n")


