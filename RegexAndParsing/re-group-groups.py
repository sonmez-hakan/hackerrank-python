import re

m = re.findall(r'(([a-zA-Z0-9])\2+)', input())
print(m[0][1]) if m else print(-1)
