arry = {2, 7, 11, 15}
target = 9


def twosum(arry, target):
    for i in arry:
        for j in arry:
            if i + j == target:
                return i, j


print(twosum(arry, target))





