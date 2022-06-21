def sort(numbers):
    int_sequence = [int(x) for x in numbers]
    return sorted(int_sequence)


str_sequence = input().split()
print(sort(str_sequence))