l = [10, 20, [30, 60, 50, [5, 6, 9, [3, 4]], 25], 45]
k = []


def flat_list(l):
    for i in l:
        #if type(i) == list:
        if isinstance(i, list):
            flat_list(i)
        else:
            k.append(i)

    return k

val = flat_list(l)
print(val)



