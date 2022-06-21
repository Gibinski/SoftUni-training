def factorial_division(num1, num2):
    return factorial(num1) / factorial(num2)

def factorial(number):
    for i in range(2, number):
        number *= i
    return number


first_num = int(input())
second_num = int(input())
result = factorial_division(first_num, second_num)
print(f"{result:.2f}")