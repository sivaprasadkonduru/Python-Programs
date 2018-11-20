import csv

'''with open('student.csv', 'r') as std:
    data = csv.reader(std)
    std_data = [i for i in data]
    print(std_data[1:])
    dict_data = csv.DictReader(std)
    std_dict = [i for i in dict_data]
    print(std_dict)'''

with open("employee.csv", 'w') as emp:
    data = csv.writer(emp)
    emp_data = [['Name', 'ID', "Org", "Desig"], ['Arjun', 12345, 'Google', "Architect"], \
                ['Krishna', 7890, 'Microsoft', "Sr. Engineer"]]
    data.writerows(emp_data)



    print(dir(data))

