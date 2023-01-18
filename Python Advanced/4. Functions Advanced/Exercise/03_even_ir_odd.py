def even_odd(*args):
    command = args[-1]
    numbers = [int(num) for num in args[:-1]]

    if command == "even":
        return [num for num in numbers if num % 2 == 0]
    else:    
        return [num for num in numbers if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
