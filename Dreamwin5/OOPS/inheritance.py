"""
Inheritance: Process of acquiring properties from an ancestor.

Types of inheritances:

Single Inheritance
Multi-Level Inheritance
Multiple Inheritance
"""

class A:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x_val(self):
        return self.x

    def get_y_val(self):
        return self.y


class B(A):

    def get_z_val(self):
        return self.z


class C(B):
    pass

class D(C):
    pass

class E(D):
    pass


obj = C(10, 30, 50)
print(obj.get_x_val())
print(obj.get_z_val())

''' = A("hello", "welcome")
obj.get_x_val()
obj.get_y_val()'''







