import numpy

M, N, P = map(int, input().split())
print(
    numpy.concatenate((
        numpy.array([input().split() for _ in range(M)], int),
        numpy.array([input().split() for _ in range(N)], int)
    ))
)
