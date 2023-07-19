from collections import OrderedDict

ordinary_dictionary = OrderedDict()

for i in range(int(input())):
    item, price = input().rsplit(' ', 1)
    price = int(price)

    if item not in ordinary_dictionary:
        ordinary_dictionary[item] = 0
    ordinary_dictionary[item] += price

for item, price in ordinary_dictionary.items():
    print(item + " " + str(price))

