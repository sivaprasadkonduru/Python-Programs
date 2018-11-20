class A:
    def foo(self):
        pass

class B:
    def foo(self):
        print('B')

class C(A, B):
    def foo(self):
        print('C')

class D(A, B):
    def foo(self):
        print('D')

class E(C, D):
    pass

obj = E()
obj.foo()
