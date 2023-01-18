rows, cols = [int(el) for el in input().split(", ")]
sum_matrix = 0
matrix = []
for _ in range(rows):
    nums = [int(el) for el in input().split(", ")]
    sum_row = sum(nums)
    sum_matrix += sum_row
    matrix.append(nums)

print(sum_matrix)
print(matrix)