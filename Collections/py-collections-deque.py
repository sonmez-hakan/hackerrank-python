from collections import deque

d = deque()
for x in range(int(input())):
    method, *args = input().split()
    getattr(d, method)(*args)

print(*d, sep=' ')