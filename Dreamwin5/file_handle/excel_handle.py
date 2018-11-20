import xlrd

#with open(r"C:\Users\User\Desktop\Books.xlsx") as xl:
wb = xlrd.open_workbook(r"C:\Users\User\Desktop\Books.xlsx")
data = wb.sheet_by_index(0)

for i in range(1, data.nrows):
    print(data.row_values(i))



