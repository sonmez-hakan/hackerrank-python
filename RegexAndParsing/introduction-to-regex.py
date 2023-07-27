import re

for t in range(int(input())):
    s = input()
    r = r'[+-]?\d+\.\d+'
    print(bool(re.fullmatch(r, s)))
