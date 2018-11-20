def fib_gen(n):

    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a+b


out = fib_gen(50)
'''print(out)
print(out.__next__())

print(out.__next__())
print(out.__next__())
for i in out:
    print(i)'''


# generator expressions

val = list((i for i in out if i % 2 == 0))
print(val)

