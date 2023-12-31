"""Write a Python function to convert more than one list to a nested dictionary.
Three Input Strings:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Output: [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}},
{'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]"""


def q(l1, l2, l3):
    result = []
    for i in range(len(l1)):
        sd = {l1[i]: {l2[i]: l3[i]}}
        result.append(sd)

    return result,


print(q(['S001', 'S002', 'S003', 'S004'], ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'],
        [85, 98, 89, 92]))
