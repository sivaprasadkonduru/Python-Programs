a = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5]

b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)
