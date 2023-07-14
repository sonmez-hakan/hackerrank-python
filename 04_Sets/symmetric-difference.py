if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))

    diff = a.symmetric_difference(b)
    for x in sorted(list(diff)):
        print(x)
