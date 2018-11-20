d = {'name': 'Raj', 'place':'Bangalore', 'company': 'Google'}

print(d.keys())
print(d.values())
print(d.items())

k = sorted(d.items(), key=lambda y: y[0])
print(k)
v = sorted(d.items(), key=lambda y: y[1])
print(v)