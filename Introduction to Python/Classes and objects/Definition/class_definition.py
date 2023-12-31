class MyClass:
    variable = 10

    def foo(self):  # We'll explain self parameter later
        print("Hello from function foo")


def bar():
    print("Hello Manthan")
    b = MyClass()
    b.foo()


a = MyClass()
print(a.variable)

a.foo()
bar()
