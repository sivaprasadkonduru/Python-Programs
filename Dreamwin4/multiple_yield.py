def hello():
    #return 'hello'
    yield 5
    yield [3, 6, 9]

    yield 'hello'

b = hello()
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

