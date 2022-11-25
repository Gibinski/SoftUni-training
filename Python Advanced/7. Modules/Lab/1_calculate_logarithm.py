from math import log, e, pi

number = int(input())
base = input()

result = log(number) if base == "natural" else log(number, int(base))

print(f"{result:.2f}")