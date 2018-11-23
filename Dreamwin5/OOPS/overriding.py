class Override:

    def __init__(self, x):
        self.x = 20

    def hello(self):
        print("I am in hello")


class XYZ(Override):

    def __init__(self, y):
        #Override.__init__(self, 20)
        super(XYZ, self).__init__(20)
        super().__init__(20)
        print(self.x)


obj = XYZ(10)

