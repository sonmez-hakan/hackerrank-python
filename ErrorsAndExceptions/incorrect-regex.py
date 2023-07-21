# pypy 3
import re

for t in range(int(input())):
    try:
        re.compile(input())
        print("True")
    except re.error:
        print("False")