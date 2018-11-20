
x = "python" # global var

def scopes():

    global x
    a = 10  # local var
    b = "hello" # local var
    x = "welcome" # local var

    print(b + " " + x)

scopes()
print(x)
#print(b)



