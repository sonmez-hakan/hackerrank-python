n = int(input())
s = set(map(int, input().split()))
N = int(input())
for x in range(N):
    strings = input().split()
    cmd = strings[0]
    num = 0
    if len(strings) == 2:
        num = int(strings[1])

    if cmd == 'pop':
        s.pop()
    elif cmd == 'remove':
        s.remove(num)
    elif cmd == 'discard':
        s.discard(num)
print(sum(s))