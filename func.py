def func_name():  # function definition
    c = 'hello' + 'python'
    print(c)


#func_name()  # function calling

"""type of arguments
Positional arguments
Default arguments
Variable no.of arguments (*args)
Keyword arguments (**kwargs)
"""

#print('defining a function')
def hello(a, b, d=10):
    print(d)
    if type(a) == str and type(b) == str:
        c = a + b
        print(c)
    else:
        print("Please provide arguments of same type")


#hello('welcome', 'python')
#hello('welcome', 20)






