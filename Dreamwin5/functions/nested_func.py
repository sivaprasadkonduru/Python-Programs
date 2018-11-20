''' Program to tell how nested functions work'''

# global

x = "global"

def outer():
    x = "nonlocal"
    def inner():
        nonlocal x
        x += "hello"
        print(x)
    print(x)
    return inner
print(x)

m = outer()
#print(m.__name__)
print(dir(m))
print(m.__closure__[0].cell_contents)
m()

print(x)

'''a = 10
def hello():
    #a = 10
    global a
    a = a + 20 # a = a + 20
    print(a)

hello()'''





