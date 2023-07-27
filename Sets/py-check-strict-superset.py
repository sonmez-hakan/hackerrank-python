if __name__ == '__main__':
    A = set(map(int, input().split()))
    lenA = len(A)
    result = True
    T = int(input())
    for t in range(T):
        B = set(map(int, input().split()))
        lenB = len(B)
        if not (len(B.difference(A)) == 0 and lenA != lenB):
            result = False
            break

    print(result)
