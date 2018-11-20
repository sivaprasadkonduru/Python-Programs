class A:

    def __init__(self, func):
        print("I am in init method")
        self.func = func

    def __call__(self, x, y):
        print("I am in call method")
        if x > 0 and y > 0:
            out = self.func(x, y)
            print(out)
        else:
            raise ValueError('x and y should br greater than zero')

@A  #div = A(div)
def div(x, y):
    return x / y


#obj = A(div)
div(20, 10)

