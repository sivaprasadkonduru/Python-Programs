''' single inheritance'''

class A:
    pass

class B(A):
    pass

''' multi-level inheritance '''

class A:
    pass

class B(A):
    pass

class C(B):
    pass

''' multiple inheritance'''

class A:
    pass

class B:
    pass

class C(B, A):
    pass

''' Hierarichal inheritance'''

class A:
    pass

class B(A):
    pass

class C(A):
    pass

''' Hybrid Inheritance'''
class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(C, B, A):
    pass
