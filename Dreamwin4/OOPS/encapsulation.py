class Vehicle:

    color = 'yellow'
    max_speed = 200
    __start_type = 'button' #private variable

    def drive(self, vtype):
        return 'I am driving {} {} with speed {}'.format(self.color, vtype, self.max_speed)

    def __start(self): # private method
        print('start the car by pressing start {}'.format(self.__start_type))


class Car(Vehicle):
    pass

obj = Car()
print(dir(Car))
print(obj.color)
print(obj.max_speed)
#print(obj._Car___start_type)
print(Vehicle._Vehicle__start_type)
print(obj.drive('Car'))
Vehicle._Vehicle__start(obj)
