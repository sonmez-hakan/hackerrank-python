def print_formatted(number):
    last = bin(number)[2:]
    length = len(last)
    for i in range(1, number + 1):
        print(
            str(i).rjust(length)
            + str(oct(i)[2:]).rjust(length + 1)
            + str(hex(i)[2:]).upper().rjust(length + 1)
            + str(bin(i)[2:]).rjust(length + 1)
        )


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
