# Q3: Write a Python program to find the first non-repeated element in a list.

lst = [1, 2, 3, 4, 2, 3, 4, 5, 7]
n_l = {}
for i in lst:
    if i in n_l:
        n_l[i] += 1
    else:
        n_l[i] = 1
for i in lst:
    if n_l[i] == 1:
        print(i)
        break
