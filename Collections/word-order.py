from collections import OrderedDict

ordered_dictionary = OrderedDict()

for i in range(int(input())):
    item = input()
    if item not in ordered_dictionary:
        ordered_dictionary[item] = 0
    ordered_dictionary[item] += 1

print(len(ordered_dictionary))
print(*list(ordered_dictionary.values()))