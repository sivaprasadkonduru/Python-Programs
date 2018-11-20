num = int(input("Enter any number: "))

'''for i in range(2, num):
    if num % i == 0:
        print("{} is not a prime number".format(num))
        break
else:
    print("{} is a prime number".format(num))'''

l = []
for j in range(2, num+1):
    for i in range(2, j):
        if j % i == 0:
            #print("{} is not a prime number".format(j))
            break
    else:
        l.append(j)
        #print("{} is a prime number".format(j))


print(l)
