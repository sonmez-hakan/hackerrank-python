if __name__ == '__main__':
    s = input()
    methods = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    for method in methods:
        print(any(getattr(i, method)() for i in s))