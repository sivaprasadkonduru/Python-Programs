class A:

    def __init__(self):
        print("I am in A")


class B(A):

    '''def __init__(self):
        print("I am in B")
    '''

class C(B, A):
    '''def __init__(self):
        print("I am in C")
    '''

class D(C, B, A):
    pass


obj = D()
print(D.mro())
print(D.__mro__)




