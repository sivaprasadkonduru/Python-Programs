def x():
    def y():
        print("hello")
    return y

a = x()
print(a.__closure__)
print(type(a))
print(dir(a))
a()

'''for i in range(1, 10):
    c = 5 * i
    print(c)'''


'''def func(val):
    val += 1
    print(val)

func(1)
func(2)'''


def outer(x):
    def inner(y):
        def abc():
            z = x * y
            print(z)
        return abc
    return inner

a = outer(5)
b = a(10)
c = b()

outer(5)(10)()

'''print(a.__closure__)
for i in range(10):
    a(i)'''

