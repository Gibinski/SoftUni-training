def smallest_of_three_numbers(nums: list):
    return min(nums)

numbers = []
for i in range(3):
    numbers.append(int(input()))

min_num = smallest_of_three_numbers(numbers)
print(min_num)
