language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')

user = 'Admin'
logged_in = 'False'

if user == 'Admin' and logged_in == 'True':
    print("Admin Page")
else:
    print('wrong creds')

if not logged_in == 'True':
    print("Please Login")
else:
    print("welcome")


print("\n")

a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)
print(id(a))
print(id(b))
b = a
print(id(a) == id(b))

condition = 0    # for 0 value , it print else statement and for any other number, it prints if statement

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
