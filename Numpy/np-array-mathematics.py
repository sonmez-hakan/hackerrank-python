import numpy as np

n = list(map(int, input().split()))[0]
a = np.array([list(map(int, input().split())) for _ in range(n)])
b = np.array([list(map(int, input().split())) for _ in range(n)])
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
