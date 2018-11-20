""""
Map:
syntax: map(func, iterables)
"""

a = ["Sachin", "sourav", "virat"]

b = ["Tendulkar", "ganguly", "kohli"]

'''def func(i, j):
    return i + " " + j

c = map(func, a, b)
print(list(c))

c = map(lambda i, j: i + " " + j, a, b)

s = map(lambda x: x * x, range(5))'''

#[("Tendulkar", 9), ("ganguly", 7), ("kohli", 5)]

l = map(lambda x: (x, len(x)), b)
val = list(l)

s = sorted(val, key=lambda x: x[1])
print(s)








