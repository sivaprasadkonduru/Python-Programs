def func(n):
    print("begining of function")
    for i in range(1, n+1):
        print("value of i is %s" % i)
        yield i*i
        print("generate next value")

a = func(10)
'''print(a.__next__())
print(a.__next__())
print(a.__next__())
print(list(a))
print(list(a))'''
for i in a:
    print(i)
