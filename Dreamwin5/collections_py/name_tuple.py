from collections import namedtuple

nt = namedtuple('student', ('name', 'id', 'std_class'))

print(nt)

val = nt('raghu', 10, 5)

print(val.name, val.id, val.std_class)