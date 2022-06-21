def add_and_subtract(numbers):
    sum = sum_numbers(numbers[0], numbers[1])
    return subtract(sum, numbers[2])


def sum_numbers(a, b):
    return a + b

def subtract(a, b):
    return a - b
    

def read_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    return numbers

print(add_and_subtract(read_numbers(3)))
