from itertools import product

K, M = list(map(int, input().split()))
l = []
for k in range(K):
    l.append(list(map(int, input().split()))[1:])

s = []
for p in product(*l):
    s.append(sum([pow(i, 2, M) for i in p]) % M)

print(max(s))
