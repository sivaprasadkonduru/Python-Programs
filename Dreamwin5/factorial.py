from app_log import logger

num = int(input("Enter any number: "))
logger.info("Number provided: %s" % num)
fact = 1
if num == 0 or num == 1:
    print("Factorial is 1")
for i in range(1, num + 1):
    fact = i * fact

logger.info("Factorial of Number %s is %s:" % (num, fact))