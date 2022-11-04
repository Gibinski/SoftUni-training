rows, cols = [int(el) for el in input().split(", ")]

matrix = []
biggest_matrix = []
biggest_sum = 0

for _ in range(rows):
    row = [int(el) for el in input().split(", ")]
    matrix.append(row)

for row in range(rows - 1):
    for col in range(cols - 1):
        sum_matrix = sum([matrix[row][col], matrix[row + 1][col], matrix[row][col + 1], matrix[row + 1][col + 1]]) 
        if sum_matrix > biggest_sum:
            biggest_matrix = [matrix[row][col], matrix[row + 1][col], matrix[row][col + 1], matrix[row + 1][col + 1]]
            biggest_sum = sum_matrix

print(biggest_matrix[0], biggest_matrix[2])
print(biggest_matrix[1], biggest_matrix[3])
print(biggest_sum)