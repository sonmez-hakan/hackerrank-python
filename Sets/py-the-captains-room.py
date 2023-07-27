K = int(input())
rooms = list(map(int, input().split()))

dictionary = {}

for r in rooms:
    if dictionary.get(r) is None:
        dictionary[r] = 0
    dictionary[r] += 1

captain = 0
for key, val in dictionary.items():
    if val != K:
        captain = key
print(captain)