def even_numbers(sequence):
    int_sequence = [int(x) for x in sequence]
    is_even = lambda x: int(x) % 2 == 0
    return list(filter(is_even, int_sequence))


str_sequence = input().split()
print(even_numbers(str_sequence))