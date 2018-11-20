x = 100 # global variable
def outer():
    #global x
    y = 10
    print('In outer function')
    def inner():
        global y
        print('Inner function')
        print(x)
        #y = 50
        print(y)


    return inner
a = outer()
a()
print(x)
#print(y)