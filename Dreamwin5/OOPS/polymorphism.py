class Poly:
    """
    A class to define method overloading.
    """
    def __init__(self, a):
        self.a = a

    def abc(self, *args, **kwargs):

        self.x = args[0] * self.a
        self.y = args[1] * self.a
        self.z = args[2] * self.a

        print(self.x, self.y, self.z)


obj = Poly(10)
obj.abc(50, 60, 70)

