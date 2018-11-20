try:
    a = 10
    b = 20
    c = 'hello'
    #import pdb

    #pdb.set_trace()
    d = a + b
    print(d)

    #x = d / 0

except (TypeError, KeyError, NameError, AttributeError) as err:
    print(err.__class__.__name__)
    print("Type error")

except Exception as err:
    print(err)
    print(err.__class__.__name__)
    print("In exception")

else:
    print("I am in else block")

finally:
    print("I am in finally")
