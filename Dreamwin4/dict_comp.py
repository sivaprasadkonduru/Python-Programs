"""
Dictionary Comprehension
syntax:  {key:value <loop> <optional_condition>}
"""

a = [9, 3, 4, 1, 2, 9, 4, 2, 1, 6, 3, 2, 4]

d = {}
for i in set(a):
    d[i] = a.count(i)
print(d)

dc = {i: a.count(i) for i in set(a) if i % 2}
print(dc)

s = """extends the descriptor protocol to include the new optional __set_name__() method.
    Whenever a new class is defined, the new method will be called on all descriptors included 
    in the definition, providing them with a reference to the class being defined and the name 
    given to the descriptor within the class namespace. In other words, instances of descriptors
    can now know the attribute name of the descriptor in the owner class:"""

l = [i for i in s.split() if len(i) > 10]
print(l)

dc = {i: len(i) for i in s.split() if len(i) > 9}
print(dc)

dt = {i: i**2 if i % 2 == 0 else i**3 for i in range(10)}
print(dt)

lc = [(i, i**2) if i%2 == 0 else (i, i**3) for i in range(10)]
print(lc)

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
p = {x: len(x) for x in names}
print(p)





