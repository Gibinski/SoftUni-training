n = int(input())

diagonal = 0
for row in range(n):
    line = input().split()
    diagonal += int(line[row])

print(diagonal)