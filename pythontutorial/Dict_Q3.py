# Write a function to multiply all the items(values) in a dictionary.
def test(test_dict):
    multiply = 1
    for i in test_dict.values():
        multiply = multiply * i
    return multiply


print(test({1: 2, 3: 4, 4: 3, 2: 1, 0: 6}))
