from itertools import combinations

string, num = input().split()
string = sorted(string)
com = list([])
for i in range(1, int(num) + 1):
    com += sorted(list(combinations(string, i)))

for c in com:
    print(''.join(c))
