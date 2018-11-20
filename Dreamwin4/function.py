def hello():
    print('hello')

a = hello

def xyz(a):
    return a

b = xyz(a)
b()

def outer():
    print('I am in outer function')
    y = 'python'
    def inner():
        print("I am in inner function")
        print(y)
    return inner

z = outer()
z()


