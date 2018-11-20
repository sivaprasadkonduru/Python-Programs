
def permutations(val):
    if len(val) == 1:
        return val

    perms = []
    for i in val:
        for perm in permutations(val.replace(i,'',1)):
            perms.append(i+perm)

    return set(perms)

permutations('abs')