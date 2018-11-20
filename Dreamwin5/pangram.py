s = "abcdefghijklmnopqrstuvwxyz"

s1 = "The quick brown fo jumps over the lazy dog"

for i in s:
    if i not in s1:
        print("Not a Panagram")
        break
else:
    print("It's a Panagram")
