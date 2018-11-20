a = [3, 4, 5]
b = [7, 8, 9]

#c = [(3, 7), (4, 8), 5, 9]
c = []
for i in enumerate(a): #(0, 3)
    for j in enumerate(b): #(0, 7)
        if i[0] == j[0]:
            c.append((i[1], j[1]))

print(c)
