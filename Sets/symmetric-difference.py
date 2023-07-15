if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))

    print('\n'.join(map(str, list(a.symmetric_difference(b)))))
