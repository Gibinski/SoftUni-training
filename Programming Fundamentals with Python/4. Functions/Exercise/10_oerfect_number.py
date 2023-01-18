def perfect_number(number):
    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum += divisor
    if sum == number:
        return "We have a perfect number!"
    return "It's not so perfect."


num = int(input())
print(perfect_number(num))