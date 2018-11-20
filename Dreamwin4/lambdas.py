a = ['hello', 'welcome', 'to', 'python', 'and', 'java']

b = [('Sachin', 500, 50), ('virat', 250, 35), ('sourav', 350, 40),
     ('yuvraj', 400, 38), ('sehwag', 350, 36)]

z = sorted(b, key=lambda x: x[2], reverse=True)
print(z)

'''o/p: [('hello', 5), ('welcome', 7), ('to', 2), 
('python', 6), ('and', 3), ('java', 4)]'''

'''b = []
def find_len(a):
    for i in a:
        b.append((i, len(i)))
    print(b)
find_len(a)'''

#def find_len(i):
#    return (i, len(i))

c = list(map(lambda i: (i, len(i)), a))
print(c)

d = list(map(lambda i: i ** 3, range(5)))
print(d)

l = list(map(lambda i: i%2, range(10)))
print(l)
e = tuple(filter(lambda i: i%2==0, range(50)))
print(e)


