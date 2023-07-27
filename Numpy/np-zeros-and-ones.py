import numpy

arr = list(map(int, input().split()))
print(numpy.zeros(tuple(arr), dtype=numpy.int))
print(numpy.ones(tuple(arr), dtype=numpy.int))
