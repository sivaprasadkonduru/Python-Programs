a = 'welcome to python'  # global variable

def func_scope():

    global x
    x = 10  # local variable
    y = 20  # local variable
    z = 'hello'  # local variable
    b = a * x
    print(b)
    

func_scope()
print(a)
print(x)