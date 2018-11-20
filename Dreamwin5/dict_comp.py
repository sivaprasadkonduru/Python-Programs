"""
dict comprehension:

syntax: {var:expression <loop> <optional condition>}
"""

d = {i: i ** 3 for i in range(5)}
print(d)

p = "hello welcome to python and it is an object oriented programming language."
c = {i: len(i) for i in p.split() if len(i) >= 5}
print(c)



