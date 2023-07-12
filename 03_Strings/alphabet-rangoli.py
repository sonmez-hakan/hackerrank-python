def print_rangoli(size):
    total = (size - 1) * 2
    highest = 96 + size
    for x in range(0, size):
        make_str(x, highest, total)

    for x in reversed(range(0, size - 1)):
        make_str(x, highest, total)


def make_str(limit, highest, total):
    string = ""
    for y in range(0, limit):
        string += chr(highest - y) + "-"
    print((string + chr(highest - limit) + string[::-1]).center(total * 2 + 1, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
