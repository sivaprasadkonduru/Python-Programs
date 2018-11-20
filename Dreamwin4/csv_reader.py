import csv
csv_data = [['name', ' age', ' sal', ' place'], ['raj', ' 25', ' 30000', ' bangalore'],
            ['ashok', ' 22', ' 20000', ' hyderabad'], ['jagan', ' 25', ' 40000', ' chennai'],
            ['anil', ' 20', ' 20000', ' mumbai'], ['raju', ' 30', ' 30000', ' hyderabad']]
#f = open("C:/Users/User/Desktop/student.csv")

with open('student_data.csv', 'w') as f:
    data = csv.writer(f)
    data.writerows(csv_data)


