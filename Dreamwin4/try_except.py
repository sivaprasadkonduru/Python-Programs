n = int(input("Enter any number: "))
d = int(input("Enter other number: "))
if d == 0:
    raise ZeroDivisionError('d cannot be zero')
try:
    a = n * 10
    b = n + 10
    if d == 0:
        raise ZeroDivisionError
    else:
        c = n / d

except Exception as err:
    print(err.__class__.__name__)

except (NameError, TypeError, ZeroDivisionError):
    print("Exception occurs")

else:
    print("I am in else block")

finally:
    print("finally")

#print(a)
#print(b)



