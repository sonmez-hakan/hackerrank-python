
if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    happiness = 0
    for x in arr:
        if x in a:
            happiness += 1
        if x in b:
            happiness -= 1

    print(happiness)
