n = int(input())
matrix = []

for _ in range(n):
    matrix.append(input())

symbol = input()

for row in matrix:
    if symbol in row:
        for col in row:
            if symbol == col:                
                result = matrix.index(row), row.index(col)
                print(result)
                break
        else:
            continue
        break
else:
    print(f"{symbol} does not occur in the matrix")