# 0 is positive even number

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
commands = input()

if commands == "even":
    for i in range(len(numbers) -1, -1, -1):
        if numbers[i] % 2 != 0:
            numbers.pop(i)
elif commands == "odd":
    for i in range(len(numbers) -1,-1, -1):
        if numbers[i] % 2 == 0:           
            numbers.pop(i)
elif commands == "negative":
    for i in range(len(numbers) -1, -1, -1):
        if numbers[i] >= 0:
            numbers.pop(i)
else:
    for i in range(len(numbers) -1, -1, -1):
        if numbers[i] < 0:
            numbers.pop(i)

print(numbers)