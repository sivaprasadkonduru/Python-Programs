palindrom_list = []
def palindrome(x, y):

    for i in range(x, y + 1):
        i1 = int(str(i)[::-1])

        if i == i1:
            palindrom_list.append(i)
    return len(palindrom_list)

palindrome(10, 50)

