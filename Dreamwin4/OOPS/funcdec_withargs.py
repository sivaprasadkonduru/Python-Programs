def dec_args(x, y):  # func1
    def func_dec(func):  # func2
        def inner_func(*args):  # func3
            print(x, y)
            print(args)
            func(*args)
        return inner_func
    return func_dec


@dec_args(3, 4)
def func_args(*args):
    return args


'''out = dec_args(3, 4)
print(out)
val = out(func_args)
print(val)'''
func_args(5, 10, 'python')
#func_args(5, 10, 'python')
