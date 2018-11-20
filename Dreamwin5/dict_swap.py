d = {'x': 1, 'y': 2, 'z': 3}

c = {}

for key, value in d.items():
    c[value] = key

print(c)