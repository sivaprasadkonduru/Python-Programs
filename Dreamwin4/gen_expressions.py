'''
syntax: (<expression> or <loop var> <for_loop> <optional_condition>)
'''

l = [i*i for i in range(5)]
print(l)

g = (i*i for i in range(5))
print(g.__next__())
print(list(g))
