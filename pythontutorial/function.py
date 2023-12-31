
def hello_func():
    print("Hello Function!")


hello_func()
print(hello_func)


def helloo_func(greetings, name="you"):
    return '{}, {}'.format(greetings, name)


print(helloo_func('Hi', name = 'Corey'))

def student_info(*args, **a):
    print(args)
    print(a)
student_info('Math', 'arts', name= "John", age =12)


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap_year(2016))

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap_year(year):
        return 29
    return month_days[month]


print(days_in_month(2017, 1))
