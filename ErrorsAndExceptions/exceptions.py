t = int(input())

for i in range(t):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)