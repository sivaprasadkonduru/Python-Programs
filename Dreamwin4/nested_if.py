marks = float(input("Enter a value: "))

if marks >= 75:
    if (marks >= 75) and (marks < 90):
        print('Grade A')
    elif marks >= 90:
        print('Grade A+')

elif (marks < 75) and (marks >= 60):
    print('First class')

elif (marks < 60) and (marks >= 50):
    print('Second class')

elif (marks < 50) and (marks >= 40):
    print('Third class')

else:
    print("Fail")
