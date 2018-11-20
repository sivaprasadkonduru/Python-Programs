#a = 50
def counter():
    a = 50
    def val():
        nonlocal a
        a = 20
        #a = a + 30
        print(a)

    print(a)
    return val

x = counter()
#print(a)
x()
'''x = counter()
#print(dir(x))
x()
#y = counter()
x()
#z = counter()
x()'''