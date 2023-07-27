import re

for x in range(int(input())):
    print('YES' if re.findall(r'^[789]\d{9}$', input()) else 'NO')
