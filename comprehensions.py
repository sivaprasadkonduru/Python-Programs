"""
List Comprehension:

syntax: [<loop_var or expression> <loop> <optional_condition>]

"""
'''a = [3, 4, 5, 6, 7]

# using loop
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)
# using map
#c = list(map(lambda i: i*i, a))
c = list(filter(lambda i: i%2 == 0, range(50)))
print(c)

# using comprehensions
#d = [i*i for i in a]
d = [i for i in range(50) if i%2 == 0]
print(d)
s = {i*i for i in a}
print(s)'''

a = [5, 6, 7, 8]
b = [50, 60, 70, 80]
c = []
for i in enumerate(a):
    for j in enumerate(b):
        if i[0] == j[0]:
            c.append((i[1], j[1]))
print(c)
# nested for loops
l = [(i[1], j[1]) for i in enumerate(a) for j in enumerate(b) if i[0] == j[0]]
print(l)

d = [i for i in range(50) if i%3 == 0 if i % 5 == 0]
print(d)

e = [(i, 'Even') if i%2 == 0 else (i, 'Odd') for i in range(10)]
print(e)

arr1 = [1, 2, 4, 5, 7]
arr2 = [5, 6, 3, 4, 8]
x = [(i, j) for i in arr1 for j in arr2 if i+j == 9]
print(x)








