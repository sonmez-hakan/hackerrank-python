if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        a = int(input())
        A = set(map(int, input().split()))
        b = int(input())
        B = set(map(int, input().split()))
        print(len(A.difference(B)) == 0)
