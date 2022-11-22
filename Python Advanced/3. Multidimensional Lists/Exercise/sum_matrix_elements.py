def read_line():
    numbers = []
    for el in input().split(", "):
        numbers.append(int(el)) 
    return numbers

n, m = read_line()
matrix = []
sum_ = 0
for i in range(n):
    matrix.append(read_line())
    sum_ += sum(matrix[i])
print(sum_)
print(matrix)