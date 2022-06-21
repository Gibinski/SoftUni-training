def odd_and_even_sum(str_nums):
    int_nums = [int(num) for num in str_nums]
    sum_of_odd_digits = sum(list(filter(lambda x: x % 2 != 0, int_nums)))
    sum_of_even_digits = sum(list(filter(lambda x: x % 2 == 0, int_nums)))
    print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")

numbers = input()
odd_and_even_sum(numbers)