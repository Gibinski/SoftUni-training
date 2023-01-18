def characters_in_range(numbers):
    letter_list = []
    for i in range(numbers[0] + 1, numbers[1]):
        letter_list.append(chr(i)) 
    return letter_list

def read_input(func, num):
    num_list = []
    for i in range(num):
        num_list.append(func(input()))
    return num_list

result =  characters_in_range(read_input(ord, 2))
print(" ".join(result))