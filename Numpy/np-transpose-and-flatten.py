import numpy

arr = numpy.array([list(map(int, input().split())) for _ in range(list(map(int, input().split()))[0])])
print(arr.transpose())
print(arr.flatten())
