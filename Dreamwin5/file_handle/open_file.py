f = open(r"C:\Users\User\Desktop\hello.txt", 'r')
#print(dir(f))
f.seek(10)
data = f.read(100)  # returns entire content from the file as string.

print(type(data), data)

data1 = f.readline()

print("readline data: %s" % (data1))

data2 = f.readlines()  # returns list of strings.
print("readlines data: %s" % data2)

