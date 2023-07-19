from itertools import permutations

string, num = input().split()
per = list(permutations(string, int(num)))

for p in sorted(per):
    print(''.join(p))