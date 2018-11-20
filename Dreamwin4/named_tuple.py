from collections import namedtuple

#t = (3, 4, 5, 'hello')

t = namedtuple('nt', 'name age place')
print(dir(t))
print(t._fields)
c = t('raj', 25, 'bangalore')
print(c, c.name, c.age, c.place, c[0], c[1], c[2])

