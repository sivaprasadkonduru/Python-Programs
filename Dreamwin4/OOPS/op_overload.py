class OpOverload:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hello(self):
        '''

        :return: returns the multiplication of two args
        '''
        self.z = self.x * self.y

    def __str__(self):
        return '{} * {} is: {} '.format(self.x, self.y, self.z)

    def __add__(self, other):
        print('In add')
        #z= self + other
        #print(z)
        a = self.x + other.x
        b = self.y + other.y
        print(a + b)

    def __sub__(self, other):
        '''
        method to perform substraction
        :param other:
        :return: interger value
        '''
        print('In sub')
        a = self.x - other.x
        b = self.y - other.y
        print(a - b)

    def __lt__(self, other):
        print('less than')


obj = OpOverload(10, 20)
obj1 = OpOverload(30, 40)
print(obj.hello())
print(obj.hello.__doc__)
print(obj)
obj + obj1
obj - obj1
obj < obj1

