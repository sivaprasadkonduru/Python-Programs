# Program to move zeros to the end of the list.

lst = [1, 7, 0, 4, 0, 9, 0, 8, 0, 3, 0]

n = len(lst)

lst[:] = filter(None, lst)

lst.extend([0] * (n - len(lst)))

print(lst)


