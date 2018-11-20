n = int(input("Enter any value: "))
m = input("Enter other value: ")

#s = 'I have %d legs and %s hands' % (n, m)

s = 'I have () legs and [] hands'.format(n)
print(s)