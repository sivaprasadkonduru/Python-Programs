''' function with args
positional args: a, b
default args: c
var no. of args: *args
keyword args: **kwargs
'''
def func_args(a, b, c=50, *args, **kwargs):

    d = a + b + c
    m = a * b * c

    return d, m, args, kwargs

x, y, z, d = func_args(10, 20, 40, 50, 60, 80, name="Dreamwin", place='Bangalore')
print(x)
print(y)
print(z)
print(d)