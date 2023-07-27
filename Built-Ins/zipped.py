students, subjects = map(int, input().split())
l = list()
for s in range(subjects):
    l.append(list(map(float, input().split())))

for z in zip(*l):
    print(sum(z) / len(z))
