def hello(p, m):
    def dec_fun(func):
        def inner(a, b):
            l = []
            if a > 0 and b > 0:
                for i in range(p):
                    c = func(a, b)
                    l.append(c * m)
                return l
            else:
                return "Please provide positive integers."
        return inner
    return dec_fun

@hello(5, 10)
def add(x, y):
    return x + y

'''out = hello(5, 10)
p = out(add)
s = p(10, 20)
print(s)'''

# wrapping a decorator
val = add(10, 20)
print(val)

# single line function call
val1 = hello(5, 10)(add)(10, 20)
print(val1)

'''
@dec_fun
def div(x, y):
    return x / y

@dec_fun
def mul(x, y):
    return x * y

@dec_fun
def mod(x, y):
    return x % y

@dec_fun
def sub(x, y):
    return x - y


val = add(10, 20)'''

'''z = dec_fun(xyz)
val = z(10, 0)'''
#print(val)