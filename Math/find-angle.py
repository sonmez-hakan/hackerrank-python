from math import degrees, atan

ab = int(input())
bc = int(input())

print(str(round(degrees(atan(ab / bc)))) + chr(176))