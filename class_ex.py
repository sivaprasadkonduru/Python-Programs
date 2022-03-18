class Hello:
    x = "shiva"

    def get_val(self, name=None):
        self.x = Hello.x


class Python(Hello):

    def print_val(self):
        print(self.x)

obj = Python()
obj.get_val()
obj.print_val
obj.print_val()
