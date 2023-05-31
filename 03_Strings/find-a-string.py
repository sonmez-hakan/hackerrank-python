def count_substring(string, sub_string):
    occurrences = 0
    for pos_x in range(0, len(string) - len(sub_string) + 1):
        match = True
        for pos_y in range(0, len(sub_string)):
            if string[pos_x + pos_y] != sub_string[pos_y]:
                match = False
            if not match:
                break
        if match:
            occurrences += 1

    return occurrences


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)