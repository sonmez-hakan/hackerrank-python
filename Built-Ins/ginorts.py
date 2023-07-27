def st(c):
    c = ord(c)
    if c >= 97:
        return 100 + c
    elif c >= 65:
        return 300 + c
    elif c % 2 == 1:
        return 400 + c
    else:
        return 500 + c


l = list(input())
l.sort(key=st)
print(''.join(l))
