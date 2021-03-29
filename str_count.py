''' Python program to convert string into character count.
i/p: "abbcccdeeaa"
o/p: "a1b2c3d1e2a2"
'''

word = "abbcccdeeaa"

def string_count(word):
    count = 1
    length = ''
    for i in range(1,len(word)):
      if word[i-1]==word[i]:
        count+=1
      else :
        length += word[i-1]+str(count)
        count=1
        
    length += word[i]+str(count)
    print(length)

string_count(word)
