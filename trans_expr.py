""" Python program to transform the expression postfix"""


def transform(expr):

    data = []
    count = 1
    for i in expr[1:]:
        if i == '(':
            count += 1
        elif i.isalpha():
            print(i, end='')
        elif i == ')':
            count -= 1
            print(data.pop(), end='')
        else:
            data.append(i)
    print()

transform('(a+(b*c))')
transform('((a+b)*(z+x))')
transform('((a+t)*((b+(a+c))^(c+d)))')