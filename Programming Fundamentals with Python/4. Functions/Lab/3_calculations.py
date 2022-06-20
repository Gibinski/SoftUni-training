def calculations(operator, num_1, num_2):
    resule = 0
    if operator == "multiply":
        result = num_1 * num_2
    elif operator == "divide":
        if num_2 != 0:
            result = num_1 // num_2
        else:
            print("Zero divide")
    elif operator == "add":
        result = num_1 + num_2
    elif operator == "subtract":
        result = num_1 - num_2
    return result

operator = input()
first_number = int(input())
second_number = int(input())

print(calculations(operator, first_number, second_number))