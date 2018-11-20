a = [1, 2, 3]
b = [4, 5, 6]

c = []
for i in enumerate(a): #outerloop
    for j in enumerate(b): #innerloop
        if i[0] == j[0]:
            c.append((i[1], j[1]))
print(c)