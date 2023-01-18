rows = int(input())

result = []
for _ in range(rows):
    row = input().split(", ")
    result.extend(map(int, row))

print(result)