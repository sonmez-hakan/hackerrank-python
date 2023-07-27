k = int(input())
arr = list(map(int, input().split()))
print(all([a > 0 for a in arr]) and any([str(a) == str(a)[::-1] for a in arr]))