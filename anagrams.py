a = ['abc', 'bac', 'cab', 'xyz', 'yzx', '123', '231']
dt = {}
dt1 = {}

def anagrams(a):

    for i in a:
        for j in a:
            if i not in dt:
                dt[i] = []
            else:
                d = ''.join(sorted(j))
                if d not in dt1:
                    dt1[j] = []
                else:
                    dt1[d].append(j)
            print(dt1)
        #print(dt)
anagrams(a)

