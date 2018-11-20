''' 0 1 1 2 3 5 8 13 21 34 '''

import pdb

n = int(input('Enter any number: '))

a = 0
b = 1

for i in range(n):
    #pdb.set_trace()
    if a > n:
        break
    print(a)
    a, b = b, a+b








