import re

for i in range(int(input())):
    s = input()
    m = re.findall(r'<[A-Za-z]+[A-Za-z0-9_\.-]+@[A-Za-z]+\.[A-Z|a-z]{1,3}>', s)
    if m:
        print(s)
