n = int(input())
s = set(map(int, input().split()))
N = int(input())
for x in range(N):
    cmd, num = list(input().split())
    s2 = set(map(int, input().split()))

    if cmd == 'intersection_update':
        s.intersection_update(s2)
    elif cmd == 'update':
        s.update(s2)
    elif cmd == 'symmetric_difference_update':
        s.symmetric_difference_update(s2)
    elif cmd == 'difference_update':
        s.difference_update(s2)

print(sum(s))
