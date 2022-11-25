def print_triangle(size: int):
    for row in range(1, size + 1):
        for num in range(1, row + 1):
            print(num, end=" ")
        print()
    for row in range(1, size):
        for num in range(1, size - row + 1):
            print(num, end=" ")
        print()