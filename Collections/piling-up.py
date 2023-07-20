from collections import deque


def pilling(d):
    while d:
        if d[0] >= d[-1]:
            last = d.popleft()
        else:
            last = d.pop()

        if len(d) == 0:
            return "Yes"

        if d[-1] > last or d[0] > last:
            print("No")


if __name__ == '__main__':
    for x in range(int(input())):
        c = int(input())
        d = deque(list(map(int, input().split())))
        print(pilling(d))
