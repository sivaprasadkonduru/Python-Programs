"""
syntax: f = open('filepath', 'mode')
"""
#f = open(r'C:\Users\User\Desktop\hello.txt')
"""print(f.tell())
f.seek(10)
print(f.tell())
for i in range(5):
    print(f.readline())

data = f.readlines()
print(data)"""

'''f = open('hello.txt', 'a')
f.write('welcome to python.\n')
print(f.tell())
f.write('Python is a dynamic typing language.\n')
f.write('python supports OOP.\n')
f.writelines(['python is an interpreted language.\n', 'Python supports web-development.\n', 'Python is easy.'])
f.close()'''

with open('hello.txt') as f:
    #data = f.read()
    #data = f.readlines()
    for i in f:
        print(i)