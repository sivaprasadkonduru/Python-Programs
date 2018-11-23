'''
oldstyle classes in py2
class Name:
    pass

Newstyle classes in py2
class Name(object):
    pass
'''

class Name:

    # class variables
    x = 10
    y = "hello"

    def __init__(shiva, a, b):
        # instance variables
        shiva.a = a
        shiva.b = b
    
    def hello(self):
        c = self.a + self.b
        print(c)


obj = Name(10, 50)  # creating and initializing an object.
print(obj.a, obj.b)
print(Name.x, Name.y)
obj.hello()  # calling a hello method through object
Name.hello(obj)  # calling hello method through class

del obj

obj.hello()

#obj1 = Name()
