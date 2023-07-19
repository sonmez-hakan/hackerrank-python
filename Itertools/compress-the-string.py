from itertools import groupby

print(*[(len(list(group)), int(key)) for key, group in groupby(input())])
