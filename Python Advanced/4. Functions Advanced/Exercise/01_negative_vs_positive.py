numbers = [int(el) for el in input().split()]


def sum_numbers(command: str, numbers: list):
    if command == "negative":
        reworked_list = [num for num in numbers if num < 0]
    else:
        reworked_list = [num for num in numbers if num > 0]

    sum_list = sum(reworked_list)
    print(sum_list)
    return sum_list


sum_negative = sum_numbers("negative", numbers)
sum_positive = sum_numbers("positive", numbers)

if abs(sum_negative) > sum_positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
