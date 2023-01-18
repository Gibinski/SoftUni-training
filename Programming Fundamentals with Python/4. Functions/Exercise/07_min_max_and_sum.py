def min_max_and_sum(numbers):
    int_sequence = [int(x) for x in numbers]

    minimum_number = min(int_sequence)
    maximum_number = max(int_sequence)
    sum_of_all_numbers = sum(int_sequence)

    print(f"The minimum number is {minimum_number}")
    print(f"The maximum number is {maximum_number}")
    print(f"The sum number is: {sum_of_all_numbers}")


str_sequence = input().split()
min_max_and_sum(str_sequence)