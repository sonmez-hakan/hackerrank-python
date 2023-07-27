from itertools import combinations

N = int(input())
letters = input().split()
K = int(input())

com = list(combinations(letters, K))

print(sum('a' in c for c in com) / len(com))
