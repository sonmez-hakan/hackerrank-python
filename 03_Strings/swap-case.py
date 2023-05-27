def swap_case(s):
    res = ""
    for index in range(0, len(s)):
        if s[index].islower():
            res = res + s[index].upper()
        else:
            res = res + s[index].lower()

    return res


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)