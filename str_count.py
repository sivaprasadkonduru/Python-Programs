''' Python program to convert string into character count.
i/p: "abbcccdeeaa"
o/p: "a1b2c3d1e2a2"

i/p: "aaaxyyccccddeaa"
o/p: "a3x1y2c4d2e1a2"
'''

word = "aaaxyyccccddeaa"

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
    return length

out = string_count(word)
print(out)
