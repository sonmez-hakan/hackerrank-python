if __name__ == '__main__':
    N = int(input())
    array = []
    for _ in range(0, N):
        words = input().split()
        if words[0] == 'insert':
            array.insert(int(words[1]), int(words[2]))
        elif words[0] == 'append':
            array.append(int(words[1]))
        elif words[0] == 'remove':
            array.remove(int(words[1]))
        elif words[0] == 'pop':
            array.pop()
        elif words[0] == 'sort':
            array.sort()
        elif words[0] == 'reverse':
            array.reverse()
        else:
            print(array)