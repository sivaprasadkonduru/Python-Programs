class A:
    def hello(self):
        print("In class {}".format(A.__name__))

class B:
    '''def hello(self):
        print("In class {}".format(B.__name__))'''

class C(B, A):
    '''def hello(self):
        print("In class {}".format(C.__name__))'''

class D(C, B, A):
    '''def hello(self):
        print("In class {}".format(D.__name__))'''


obj = D()
obj.hello()

print(D.mro())  # Method Resolution Order
print(D.__mro__)


