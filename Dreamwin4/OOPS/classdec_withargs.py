class Decorator:

    def __init__(self, x):
        self.x = x

    def __call__(self, func):
        def dec_args(a, b):
            out = func(a, b)
            return out
        return dec_args


@Decorator(5)
def hello(a, b):
    return a * b


'''obj = Decorator(5)
print(obj)
val = obj(hello)
print(val)'''
hello(10, 20)



