from itertools import combinations_with_replacement

string, num = input().split()
com = list(combinations_with_replacement(sorted(string), int(num)))

for c in com:
    print(''.join(c))
