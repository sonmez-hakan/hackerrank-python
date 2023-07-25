from re import findall

r = findall(r"(?<=[qwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])", input())
print("\n".join(r) if r else "-1")