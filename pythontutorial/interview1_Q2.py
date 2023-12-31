# arr = [3,2,3]
# arr = [2,2,1,1,1,2,2]
from collections import Counter
def majority_element(arr):
    dic_r = Counter(arr)
    l = dic_r.values()
    m_l = max(l)
    for k, v in dic_r.items():
        if v == m_l:
            return k


x = majority_element([3, 2, 3])
print(x)
