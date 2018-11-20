marks = int(input("Enter student marks: "))

if marks >= 75:
    if marks >= 75 and marks < 90:
        print("Distinction")
    elif marks >= 90 and marks <= 100:
        print("A+")
    else:
        print("Marks cann't be greater than 100")

elif marks >= 60 and marks < 75:
    print("First Class")

elif marks >= 50 and marks < 60:
    print("Second Class")

elif marks >= 35 and marks < 50:
    print("Third Class")

else:
    print("Fail")




