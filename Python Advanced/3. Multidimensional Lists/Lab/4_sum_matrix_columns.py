rows, cols = [int(el) for el in input().split(", ")]

result = [0 for i in range(cols)]

for row in range(rows):
    line = [int(el) for el in input().split()]
    for cell in range(cols):
        result[cell] += line[cell]

print("\n".join(map(str, result)))