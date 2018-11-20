class Overload:

    '''def hello(self, a, b, c):
        d = a * b + c
        print(d)

    def hello(self, a, b):
        c = a * b
        print(c)'''

    def hello(self, *args, **kwargs):
        print(args)
        print(kwargs)

obj = Overload()
obj.hello(5, 10)
obj.hello(5, 10, 15)
obj.hello(10)

