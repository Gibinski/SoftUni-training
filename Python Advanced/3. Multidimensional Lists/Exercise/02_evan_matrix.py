from read_line import line_to_int_list

rows = int(input())
matrix = []
for i in range(rows):
    matrix.append(list(filter(lambda x: x % 2 == 0, line_to_int_list())))

print(matrix)