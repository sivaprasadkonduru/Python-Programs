class A:

    def hello(self, a, b):
        c = a * b
        print(c)


class B(A):

    def hello(self, a, b, c):
        #A.hello(a, b)
        super(B, self).hello(a, b) # super().hello(a, b))
        d = a * b + c
        print(d)


class C(B):
    def hello(self):
        A.hello(self, 10, 20)
        super().hello(10, 20, 30)
        print('In class C Hello')


obj = C()
obj.hello()
