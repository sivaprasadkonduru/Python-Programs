a = ['abc', 'bac', 'cab', 'xyz', 'yzx', '123', '231']

def anagrams(a):
    d = {}
    for i in a:
        val = ''.join(sorted(i))
        if val not in d:
            d[val] = []
        d[val].append(i)
    return d.values()

out = anagrams(a)
print(out)

