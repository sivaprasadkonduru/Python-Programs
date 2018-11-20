""" Generator """

def gen():

    yield 100
    yield "hello"
    yield [3, 4, 5]


a = gen()

print(a.__next__())

for i in a:
    print("gen_values", i)

for i in a:
    print("val", i)



