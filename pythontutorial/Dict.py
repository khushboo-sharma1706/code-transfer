student = {'name': 'John', 'age': 25, 'courses': ["Math", "CompSci"]}
print(student['name'])
print(student['courses'])

print(student.get('name'))
print(student.get('Phone'))
print(student.get('Phone', 'Not Found'))

student['Phone'] = 2736226317
print(student.get('Phone', 'Not Found'))
print(student)
student['age'] = 45
print(student)

student.update({'name': 'Jerry', 'age': 40, 'courses': ["Math", "Python"], 'Year': "3rd"})
print(student)

del student['Year']
print(student)
age = student.pop('age')
print(age)
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key,value)