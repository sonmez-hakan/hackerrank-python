from collections import namedtuple

x = int(input())
columns = input().split()
Student = namedtuple('Student', ','.join(columns))
print(sum([int(Student(*input().split()).MARKS) for i in range(x)]) / x)
