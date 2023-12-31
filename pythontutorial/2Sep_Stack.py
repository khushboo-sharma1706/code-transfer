s = []

# push
s.append(1)
s.append(2)
s.append(3)  # O(n)

# pop
print(s.pop())

# len
print(len(s))

# push -> push at top
# pop -> pull from top
# len -> length

# O(1) a = 1
# for i in range(n): -> O(n)
#    pass
# for i in range(n): -> O(n^2)
#    for i in range(n): -> O(n)
#        pass
# for i in range(n): -> O(n^3)
#   for i in range(n): -> O(n^2)
#    for i in range(n): -> O(n)
#        pass

##########################################

from collections import deque

s_d = deque()

s_d.append(1)
s_d.append(2)
s_d.append(3)

print(s_d.pop())



