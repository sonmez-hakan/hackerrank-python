def minion_game(string):
    stuart = 0
    kevin = 0
    length = len(string)
    vowels = "AEIOU"
    for index, char in enumerate(string):
        remaining = length - index
        if char in vowels:
            kevin += remaining
        else:
            stuart += remaining

    if kevin > stuart:
        print("Kevin " + str(kevin))
    elif stuart > kevin:
        print("Stuart " + str(stuart))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
