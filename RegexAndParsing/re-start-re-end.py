import re
s, k = input(), input()
m = list(re.finditer(f"(?={k})", s))
l = len(k)

print('\n'.join([str((i.start(), i.start() + l - 1)) for i in m])) if len(m) > 0 else  print((-1, -1))
