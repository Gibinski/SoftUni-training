def even_numbers(func): 
    def numbers(num):
        return [n for n in func(num) if n % 2 == 0]
    return numbers


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))