import textwrap


def merge_the_tools(string, k):
    words = textwrap.wrap(string, k)
    for index, word in enumerate(words):
        string = ""
        dic = {}
        for char in word:
            if dic.get(char) is None:
                string += char
            dic[char] = char
        print(string)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)