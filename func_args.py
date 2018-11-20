from Dreamwin4.mod_a import hello

def var_args(a, b, c=10, *args, **kwargs):
    print('a is :', a)
    print('b is :', b)
    print('c is :', c)
    print(args)
    print(kwargs)
    return a, b, c, args, kwargs

out = var_args(100, 200)
print(out)
val = var_args(10, 20,30, 40, 50, 60, 70, 80, name='python', year=1990)
print(val)

