import pdb

def outer():
    pdb.set_trace()
    print("I am in outer function")
    def inner():
        print("I am in inner function")
    return inner

a = outer()
a()



