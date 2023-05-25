grades = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    grades.append([name, score])

grades.sort(key=lambda x: x[1])
last = grades[0][1]
index = 1
names = []
for grade in grades:
    if last == grade[1]:
        if index == 2:
            names.append(grade[0])
    elif last < grade[1]:
        index += 1
        last = grade[1]
        if index == 2:
            names.append(grade[0])
        elif index > 2:
            break

names.sort()
for name in names:
    print(name)