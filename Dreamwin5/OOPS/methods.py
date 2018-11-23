class Hello:

    """
    Class to define different type of methods
    """
    a = 100
    b = 200

    # Instance method
    def imethod(self, x, y):
        print("Instance Method")
        self.x = x
        self.y = y

    @classmethod
    def cmethod(cls):
        print("class method")

    @staticmethod
    def smethod():
        print("Static Method")

obj = Hello()
obj.imethod(10, 20)
Hello.imethod(obj, 30, 40)

obj.x = 50
obj.y = 60
obj.a = 50
obj.b = 100
print(obj.x, obj.y, obj.a, obj.b)
Hello.cmethod()
obj.cmethod()

Hello.smethod()
obj.smethod()


