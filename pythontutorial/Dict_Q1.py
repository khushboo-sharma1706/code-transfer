"""Q1: Write a Python program to sort (ascending and descending) a dictionary by value.
Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Dictionary in ascending order by value:  {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
Dictionary in descending order by value:  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}"""


test_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_list = []


while len(test_dict) > 0:
    min_v = 100000000
    min_k = 200000000
    for k,v in test_dict.items():
        if v < min_v:
            min_v = v
            min_k = k
    sorted_list.append((min_k, min_v))
    print(test_dict)
    del test_dict[min_k]
print("Sorted List in ascending order : ",sorted_list)
print("Sorted List in descending order : ", sorted_list[::-1])

"""a = [10,20,30,40,5,10]
min = a[0]
for i in a:
    if i< min:
        min = i
print(min)     """
