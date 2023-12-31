def list(l):
  n = []
  for a in l:
    if a not in n:
      n.append(a)
  return n

#print(unique_list([34,5,2,78,2,9,24,6,4,4,5,6,7,88,8]))

b = (input(" Enter List elements: ") )
print(list(b))
