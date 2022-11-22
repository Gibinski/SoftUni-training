def line_to_int_list():
    line = []
    for el in input().split(", "):
        line.append(int(el)) 
    return line


def matrix_of_int(rows):
    matrix = []
    for i in range(rows):
        matrix.append(line_to_int_list)
    return matrix