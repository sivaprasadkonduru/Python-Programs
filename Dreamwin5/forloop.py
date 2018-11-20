"""
for syntax:

for <loop_var> in <iterable>:
    <block of statements>

# else block is optional
else:
    <block of statements>

"""
# iterables are an objects in python on which we can perform iterations

'''for i in "welcome":

    if i == 'o':
        continue
    print(i)

else:
    print("for loop executed successfully")
'''

l = [1, 2, 2, 5, 3, 1, 4, 7, 4, 9, 2, 3]

#d = {1: 2, 2: 3, 3: 2, 4: 2, 5: 1, 7: 1, 9: 1}

d = {}
s = set(l) #{1, 2, 4, 3, 5, 7, 9}
for i in s:
    d[i] = l.count(i) #{1: 2, 2: 3, }
print(d)

'''for i, j in enumerate(s):
    print(i, j)'''

for i, j in enumerate(d.items()):
    print(i, j)
    

