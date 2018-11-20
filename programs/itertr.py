'''
#Iterators:
       #1.Iterator is a object which implements the iterator protocol.
       #iterator consists 2methods, __iter__ and __next__
       __iter__ returns iterator object itself.
       __next__ returns the next value from the iterator.If there is no more items to return
                then it should raise stopiteration exeption.

'''

s = "python"
for e in s:
    print(e, end="")#it will return python

print() #it will return empty

n=iter(s)
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(list(n))
#print(n.__next__())# it will throw an stopIteration exception.

class pow():
     def __init__(self,max=0):
         self.max=max
     def __iter__(self):
         self.n=0
         return self
     def __next__(self):
         if self.n <= self.max:
             result=2 ** self.n
             self.n += 1
             return result
         else:
             raise StopIteration

a=pow(8)
i=iter(a)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
