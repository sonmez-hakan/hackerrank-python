lines, columns = input().split()
lines = int(lines)
columns = int(columns)
c = '.|.'

for i in range(lines // 2):
    print((c*i).rjust((columns - 3) // 2, '-')+c+(c*i).ljust((columns - 3) // 2, '-'))

print("WELCOME".center(columns, '-'))

for i in reversed(range(lines // 2)):
    print((c*i).rjust((columns - 3) // 2, '-')+c+(c*i).ljust((columns - 3) // 2, '-'))
