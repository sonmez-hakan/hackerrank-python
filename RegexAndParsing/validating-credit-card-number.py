import re

r = r'^(?!.*(\d)(-?\1){3})[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
[print('Valid') if re.findall(r, input()) else print('Invalid') for _ in range(int(input()))]
