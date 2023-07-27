import numpy

l = numpy.array([list(map(int, input().split())) for _ in range(list(map(int, input().split()))[0])])
print(l.transpose())
print(l.flatten())
