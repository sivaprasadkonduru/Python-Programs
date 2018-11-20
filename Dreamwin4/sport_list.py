''' i/p: ["sachin cricket", "Federer tennis", "Nadal tennis", "virat cricket",
"Messi football"]

o/p: {"cricket": ["sachin", "virat"], "tennis": ["federer", 'nadal'],
"football": ['Messi']}

sport = ["sachin cricket", "Federer tennis", "Nadal tennis", "virat cricket",
"Messi football"]

d = {}

for i in sport:
    s = i.split()  # ['sachin', 'cricket']
    if s[1] not in d:
        d[s[1]] = []
    d[s[1]].append(s[0])

print(d)'''

'''i/p: ['ashok', 'hari', 'bhanu', 'anil', 'bharath', 'anvesh', 'uday', 'raja']
o/p: {'a': ['ashok', 'anil', 'anvesh'], 'b': ['bhanu', 'bharath'], 'h': ['hari'], 
'u': ['uday'], 'r': ['raja']}'''

val = ['ashok', 'hari', 'bhanu', 'anil', 'bharath', 'anvesh', 'uday', 'raja']
d = {}

for i in val: # 'ashok'
    if i[0] not in d:
        d[i[0]] = []        #{'a': [], 'h':[]}
    d[i[0]].append(i)  #{'a': ['ashok'], 'h': ['hari']}

print(d)

from collections import defaultdict
df = defaultdict(set)
print(df)
for i in val:
    df[i[0]].add(i)
print(df)


a = [3, 4, 5, 6, 4, 6, 6, 4, 5]
'''o/p :{3:1, 4:3, 5:2, 6:3}'''
di = {}
#di = defaultdict(int)
for i in a:              #0 + 1
    #d[i] += 1  # d[i] = d[i] + 1
    di[i] = a.count(i)


