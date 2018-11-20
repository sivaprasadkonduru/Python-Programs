'''def hello(a, b):
    c = a + b
    return c


x = hello(10, 20)


def welcome(x):

    print(x ** 2)

welcome(x)'''


def return_multiple():
    """
    Function to return multiple values.
    input: a --> int
           b --> str
    return: it returns multiple objects ( a, b)
    """
    a = [3, 4, 5]
    b = (6, 7, 8)

    return a, b

c = return_multiple()
print(c.__doc__)
print(return_multiple.__doc__)
