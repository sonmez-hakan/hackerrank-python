def print_full_name(first, last):
    print("Hello firstname lastname! You just delved into python.".replace("firstname", first).replace("lastname", last))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)