def validate_args(func):
    def validate(m, n):
        if m > 0 and n > 0:
            #pass
            out = func(m, n)
            return out
        else:
            raise AttributeError('x and y must be greater than zero.')
    return validate

@validate_args  # decorator
def add(x, y):  # decorated function
    print('In addition')
    return x + y

#@validate_args
def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mul(x, y):
    return x * y

#add = validate_args(add)
add(10, 20)
#div(20, 10)
