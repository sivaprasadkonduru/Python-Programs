"""
syntax:

while <condition>:
    <block of statements>

else:
    <block of statements>
"""

i = 0

while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

else:
    print("while loop completed successfully")
