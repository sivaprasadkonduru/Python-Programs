class OpOverload:

    def __init__(self, x, y):
        print("In Init method")
        self.x = x
        self.y = y

    def __str__(self):
        #print("hello")
        return "hello"

    def __add__(self, a):
        self.m = self.x + a.x
        self.n = self.y + a.y
        return self.m, self.n

    def __gt__(self, a):
        return self.m > self.n

    def __lt__(self, a):
        return self.m < self.n

    def __eq__(self, a):
        return self.m == self.n

obj = OpOverload(10, 20)
#print(obj)
obj1 = OpOverload(30, 40)
print(obj + obj1)  # obj.__add__(obj1)
print(obj > obj1)
print(obj < obj1)
print(obj == obj1)