numbers = list(map(float, input().split()))
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

for value in unique:
    print(f"{value:.1f} - {numbers.count(value)} times")
