cube = lambda x: x ** 3


def fibonacci(n):
    l = [0, 1, 1]
    if n < 3:
        return l[:n]

    for t in range(3, n):
        l.append(l[t - 1] + l[t - 2])

    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
