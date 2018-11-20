class A:

    def hello(self):
        print('I am in A')

class B(A):
    def hello(self):
        print('I am in B')

class C(A):
    def hello(self):
        print('I am in C')

class D(C, B):
    def hello(self):
        print('I am in D')

obj = D()
obj.hello()
print(D.mro())  # D C B A object



