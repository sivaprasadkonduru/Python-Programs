"""
filter:
syntax: filter(func, iterable)
"""
odd = []
for i in range(10):
    if i % 2 != 0:
        odd.append(i)


a = filter(lambda x: x % 2, range(20))

print(list(a))

b = map(lambda x: x % 2==0, range(20))

print(list(b))

c = filter(lambda x: x%3 == 0 and x%5==0, range(50))
print(list(c))

l = [("Tendulkar", 9), ("ganguly", 7), ("kohli", 5)]

d = filter(lambda x: x[1] > 5, l)
print(tuple(d))

