single_string = list(map(int, input().split(", ")))
numbers = [i for i in range(len(single_string)) if single_string[i] % 2 == 0]
print(numbers)