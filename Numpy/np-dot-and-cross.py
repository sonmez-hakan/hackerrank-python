import numpy

n = int(input())
a = numpy.array([list(map(int, input().split())) for _ in range(n)])
b = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.dot(a, b))
