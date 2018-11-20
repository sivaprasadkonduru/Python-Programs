a = 10
b = 'hello'

print(globals())
def xyz():
    c = 'python'
    d = 100
    print(locals())

xyz()

