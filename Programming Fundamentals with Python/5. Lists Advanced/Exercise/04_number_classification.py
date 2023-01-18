numbers = list(map(int, input().split(", ")))
nums = [[], [], [], []]  
for num in numbers:
    if num >= 0:
        nums[0].append(num)
    if num < 0:
        nums[1].append(num)
    if num % 2 == 0:
        nums[2].append(num)
    if num % 2 != 0:
        nums[3].append(num)

print("Positive: ", end="")
print(*nums[0], sep=", ")
print("Negative: ", end="")
print(*nums[1], sep=", ")
print("Even: ", end="")
print(*nums[2], sep=", ")
print("Odd: ", end="")
print(*nums[3], sep=", ")
