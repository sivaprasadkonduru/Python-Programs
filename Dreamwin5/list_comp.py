"""
list comprehensions:
syntax: [<expression or loop_var> loop <optional_condition>]
"""

'''a = [1, 2, 3, 4, 5]

# for -loop
b = []
for i in a:
    a.append(i*i)

# map-lambda
c = map(lambda x: x*x, a)'''

l = [i*i for i in range(10) if i % 2 == 0]
print(l)

p = "hello welcome to python and it is an object oriented programming language."

x = [(i, len(i)) for i in p.split() if len(i) >= 5]
print(x)

m = [(i, 'even') if i%2==0 else (i, 'odd') for i in range(1, 10)]
print(m)

a = [2, 3, 4]
b = [5, 6, 7]

#[(2, 5), (3, 6), (4, 7)]

n = [(i[1], j[1]) for i in enumerate(a) for j in enumerate(b) if i[0] == j[0]]
print(n)




