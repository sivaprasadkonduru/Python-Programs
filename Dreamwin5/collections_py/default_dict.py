from collections import defaultdict
l = [3, 4, 2, 6, 8, 2, 4, 2, 6, 3, 6]

d = {}

for i in set(l):
    #d[i] = l.count(i)
    d[i] = d.get(i, 0) + 1

print(d)

dd = defaultdict(int)

for i in l:
    dd[i] += 1

print(dd)




pt = ["sachin cricket", "Federer tennis", "Nadal tennis", "virat cricket", "Messi football"]
out = {"cricket": ["sachin", "virat"], "tennis": ["federer", 'nadal'],
"football": ['Messi']}

# without defaultdict
pd = {}
for i in pt:
    p, s = i.split()
    if s not in d:
        pd[s] = []
    pd[s].append(p)

# with defaultdict
df = defaultdict(list)
for i in pt:
    p, s = i.split()
    df[s].append(p)

print(df)


