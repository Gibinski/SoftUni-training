def abs_numbers(numbers):
    nums = list(map(float, numbers.split(" ")))
    result = list(map(abs, nums))
    print(result)

abs_numbers(input())