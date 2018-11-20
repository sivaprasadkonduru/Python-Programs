class Temp:

    def __init__(self, temp):
        self.__temp = temp

    @property
    def get_temp(self):
        return self.__temp

    @get_temp.setter
    def set_temp(self, x):
        self.__temp = x
        return self.__temp

    @get_temp.deleter
    def del_temp(self):
        del self.__temp


obj = Temp(30)
#print(obj.temp)
'''print(obj.get_temp())
obj.set_temp(50)
print(obj.temp)'''
obj.temp = 40
print(obj.temp)
#obj.set_temp(60)
obj.set_temp = 60  # property
print(obj.temp)

print(obj.get_temp)
obj.set_temp = 100
print(obj.get_temp)

del obj.del_temp
print(obj.temp)
