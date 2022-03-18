'''Python program to check if the number is an Armstrong number or not

153 = 1 ** 3 + 5 ** 3 + 3 ** 3  // 153 is an Armstrong number.
1634 = 1 ** 4 + 6 ** 4 + 3 ** 4 + 4 ** 4  // 1634 is an Armstrong number.

'''

# take input from the user
num = int(input("Enter a number: "))
# initialize sum
sum = 0
order = len(str(num))
temp = num

# find the sum of the cube of each digit
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(f"{num} is an Armstrong number")
else:
   print(f"{num} is not an Armstrong number")
