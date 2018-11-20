class A:  # parent class
    val = 'hello'

    def __init__(self, x):
        self.x = x

    def get_value(self):
        print(self.y)


class B(A): # child class

    def __init__(self, x):
        self.y = x

    def name(self):
        print(self.y)


class C(B):
    pass

class D(C):
    pass


obj = B(10)
#print(obj.y)
obj.get_value()
print(obj.val)
obj.name()

