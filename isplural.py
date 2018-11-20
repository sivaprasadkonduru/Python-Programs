import inflection
s = input('Enter a singular word: ')
p = input('Enter a singular word: ')


def is_plural(s, p):

    word = inflection.pluralize(s)
    print(word)
    if word == p:
        return True
    else:
        return False


a = is_plural(s, p)
print(a)


