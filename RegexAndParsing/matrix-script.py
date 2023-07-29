import re

n, m = map(int, input().rstrip().split())
lines = ['' for _ in range(m)]
for _ in range(n):
    item = input()
    for y in range(0, m):
        lines[y] += item[y]

print(re.sub(r'\b\W+\b', ' ', ''.join(lines)))
