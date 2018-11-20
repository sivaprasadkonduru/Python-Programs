#ex1
def add_ing(str1):
    length = len(str1)

    if length > 2:
        if str1[-3:]=='ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    return str1

print(add_ing('lo'))
print(add_ing('abc'))
print(add_ing('applying'))

#ex2
def longest_word(words):
    list1=[]

    for i in words:
        list1.append((len(i),i))
        list1.sort()
    return list1[-1][1]

print(longest_word(["python","java","practice"]))
#ex3
def remove(str,n):
    first_part=str[:n]
    last_spart=str[n+1:]
    return first_part + last_spart

print(remove('python',0))
print(remove('python',3))
print(remove('python',5))
#ex4
def change_string(str2):
    return str2[-1:] + str2 [1:-1] +str2[:1]

print(change_string('abcd'))
print(change_string('12345'))
#ex5
def word_count(str1):
    counts=dict()
    words=str1.split()

    for i in words:
        if i in counts:
            counts[i] +=1
        else:
            counts[i] =1

    return counts

print(word_count("the quick brown is in hjcb hjfbr."))
#ex6
n=input("What's your programming language??:")
print("my fav lang is:",n.upper())
print("my fav lang is:",n.lower())
#ex7
n1=input("comma seperated words:")
l=[i for i in n1.split(",")]
print(','.join(sorted(list(set(l)))))
print(",".join(list(set(l))))
#ex8
def add(tag, word):

    return "<%s>%s</%s>" % (tag, word, tag)

print(add('i', 'python'))
print(add('b', 'python Tutorial'))
#ex9
def words(str, word):
    return str[:2]+word+str[2:]

print(words('[[]]','python'))
print(words('{{}}','php'))
print(words('<<>>','HTML'))
#ex10
def first(str):
    return str[:3] if len(str) >3 else str
print(first('python'))
print(first('ibl'))
print(first('sweety'))
#ex10
def must_length(str):
    sub_str=str[-2:]
    return sub_str * 4
print(must_length('python'))
print(must_length('sweety'))
#ex11
str1="https://www.w3resource.com/python-exercises/string"
print(str1.split('/',1)[0])
print(str1.split('-',1)[0])
#ex12: reverse string multiple by 4
def reverse_string(str):
    if len(str) %4 ==0:
        return ''.join(reversed(str))
    return str
print(reverse_string('python'))
print(reverse_string('ruby'))
print(reverse_string('loki'))
#ex13: reverse string ex1
str='abacd'
print(str[::-1])

#reversing ex2
def rversng_string(str):
    return ''.join(reversed(str))
print(rversng_string('python'))
print(rversng_string('hadoop'))
#ex:13 display a number with a comma seperated.
x=6000000
y=60000000
print("\norginal value:",x)
print("formatted number with comma separated:"+"{:,}".format(x));
print("Orginal value:",y)
print("formatted number with comma separated:"+"{:,}".format(y));
print()

#ex:14 format a number with percentage
x=-0.25
y=0.25
print("\nOrginal value",x)
print("formated number with percentage:"+"{:.2%}".format(x))
print("orginal value",y)
print("formatted numbar with percentage:"+"{:.2%}".format(y))
print()
#ex:15 reversing words
def reverse_words(str):
    for i in str.split('\n'):
        return(''.join(i.split()[::-1]))

print(reverse_words("The quick brown fox jumps over the lazy dog."))
print(reverse_words("python exercise."))
#ex:16 strip a set of characters from a string.
def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)

print("\nOrginal value: ")
print("The quick brown fox jumps over the lazy dog.")
print("After stripping a,e,i,o,u")
print(strip_chars("The quick brown fox jumps over the lazy dog.","aeiou"))
print()
#ex:17 cube of rectangle
area=1235.56
volume=345.735
decimal=2
print("The area of rectangle is{0:.{1}f}cm\u00b2".format(area,decimal))
decimal=3
print("The area of cylinder is{0:.{1}f}cm\u00b3".format(volume,decimal))
'''
#Iterators:
       #1.Iterator is a object which implements the iteratoe protocol.
       #iterator consists 2methods, __iter__ and __next__
       __iter__ returns iterator object itself.
       __next__ returns the next value from the iterator.If there is no more items to return 
                then it should raise stopiteration exeption.
                      
'''

s="python"
for e in s:
    print(e,end="")




