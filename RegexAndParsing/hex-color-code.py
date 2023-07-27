import re

valid = False
for x in range(int(input())):
    s = input()
    if not valid:
        if re.search(r'\{', s):
            valid = True
            continue
    elif re.search(r'\}', s):
        valid = False
        continue

    if valid:
        m = re.findall(r'\#[a-fA-F0-9]{3,6}', s)
        if m:
            print('\n'.join(m))
