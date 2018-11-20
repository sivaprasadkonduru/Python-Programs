class Human:

    height = 170 # class variable

    def set_weight(self, weight):
        self.weight = weight # instance variable

    def get_weight(self):
        print(self.weight)


obj = Human()  # __neww__ and __init__
print(obj.height)
obj.set_weight(55)  # obj.set_weight(obj, 55)
obj.get_weight()







