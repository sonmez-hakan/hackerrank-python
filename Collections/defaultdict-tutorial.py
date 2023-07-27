from collections import defaultdict

n, m = list(map(int, input().split()))
d = defaultdict(list)
for i in range(1, n + 1):
    d[input()].append(i)

for x in range(m):
    c = input()
    if len(d[c]) == 0:
        print(-1)
    else:
        print(*d[c])
