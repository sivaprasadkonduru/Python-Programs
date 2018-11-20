import re

a = """Hello
    welcome
    to
    python"""

b = re.findall(r".*", a, re.DOTALL)
print(b)

