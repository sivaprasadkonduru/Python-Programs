a = ["cat", "tea", "tac", "node", "ate", "cat", "done", "tab", "eat", "xyz", "bat"]

def anagrams(a):
    '''
    Function to find all anagrams:
    :param a:
    :return: list
    '''
    dt = {}
    for i in a:
        val = ''.join(sorted(i)) # 'act'
        if val not in dt:
            dt[val] = []
        dt[val].append(i)

    print(dt.values())

anagrams(a)
print(anagrams.__doc__)