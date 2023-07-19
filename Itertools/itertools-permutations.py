from itertools import combinations

string, num = input().split()
com = list(combinations(string, int(num)))

for c in sorted(com):
    print(''.join(c))
