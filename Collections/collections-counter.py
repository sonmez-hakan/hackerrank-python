from collections import Counter

X = int(input())
N = list(map(int, input().split()))
c = Counter(N)

total = 0
for x in range(int(input())):
    s, p = list(map(int, input().split()))
    if c[s] > 0:
        total += p
        c[s] -= 1

print(total)
