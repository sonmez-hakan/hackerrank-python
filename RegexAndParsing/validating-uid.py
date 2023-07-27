import re

r = r"^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)(?!.*(.).*\1)[a-zA-Z0-9]{10}$"
[print("Valid" if re.match(r, input()) else "Invalid") for _ in range(int(input()))]
