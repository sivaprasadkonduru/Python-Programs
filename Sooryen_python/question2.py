'''
Write a program that takes as input an array of numbers and outputs the average
value and the number of items in the array
'''

array = input()
array = [int(i) for i in array.split()]
no_of_items = len(array)
average = sum(array) / no_of_items

print(average)
print(no_of_items)


