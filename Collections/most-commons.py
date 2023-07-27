from collections import Counter

if __name__ == '__main__':
    for k, v in Counter(sorted(input())).most_common(3):
        print(k, v)
