n = int(input('Enter any value: '))

l = []
for j in range(2, n):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        l.append(j)

print(l)