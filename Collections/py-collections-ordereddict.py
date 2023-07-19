from collections import OrderedDict

ordered_dictionary = OrderedDict()

for i in range(int(input())):
    item, price = input().rsplit(' ', 1)
    if item not in ordered_dictionary:
        ordered_dictionary[item] = 0
    ordered_dictionary[item] += int(price)

for item, price in ordered_dictionary.items():
    print(item + " " + str(price))
