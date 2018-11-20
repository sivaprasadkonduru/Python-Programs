class Animal:
    name = 'Tiger' # class variable

    def __init__(self, place):
        self.place = place # instance variable

    def print_details(self):
        return '{} lives in {}'.format(self.name, self.place)

    def print_place(shiva):
        print(shiva.place)


obj = Animal('zoo') # creating an object/instance
print(obj.place)
print(obj.name)
print(Animal.name)
val = obj.print_details()
print(val)
obj.print_place()
a = Animal.print_details(obj)
print(a)

print(Animal.__dict__)



