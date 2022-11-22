from read_line import line_to_int_list

n, m = line_to_int_list()
matrix = []
sum_matrix = 0
for i in range(n):
    matrix.append(line_to_int_list())
    sum_matrix += sum(matrix[i])
print(sum_matrix)
print(matrix)