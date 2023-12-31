courses = ["History", "Maths", "Chemistry", "Biology", "CompSci"]
courses[0] = "Arts"
print(courses)
"""
print(courses)
print(len(courses))
print(courses[0:3])
print(courses[-1])
print(courses[-1:-3:-1])

courses.append("Arts")
courses_2 = ["Economics","Geography"]
print(courses)
courses.insert(1, "Civil")
print(courses)
courses.insert(2, courses_2)
print(courses)
courses.extend(courses_2)
print(courses)
print("\n")

courses.remove('Geography')
print(courses)
popped = courses.pop()
print(popped)
print(courses)

courses_2.reverse()
print(courses_2)

courses_2.sort()
print(courses_2)

nums = [2,4,1,5,3]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
print(sum(nums))

print(courses.index("Biology"))
print("Maths" in courses)
print("\n")
for item in courses:
    print(item)

print("\n")

for index, course in enumerate(courses, start=1):
    print(index, course)
print("\n")
"""

courses_str = ', '.join(courses)
print(courses_str)

new_list = courses_str.split(",")
print(new_list)



#Lists are mutable and Tuples are immutable - we can't modify tuples

"""tuple_1 = ("Math", "Science")
tuple_1[1] = "Physics"
print(tuple_1)"""

#Sets
print("\n")
cs_course ={"Math", "Design", "Science","Physics"}
art_course ={"History", "Design", "Geography","Economics"}

print(cs_course.intersection(art_course))
print(cs_course.difference(art_course))
print(cs_course.union(art_course))

#Empty list
empty_list =[]
empty_list = list()

# Empty Tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty set
empty_set = {} #This is not correct, its a dictionary
empty_set = set()
