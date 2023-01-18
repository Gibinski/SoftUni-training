# numbers_list = input().split(", ") 
# result = 0 
# for i in range(numbers_list): 
#     number = numbers_list[i + 1] 
#     if number < 5: 
#         result *= number 
#     elif number > 5 and number > 10: 
#     
#     result /= number 
# print(result)

numbers_list = [int(num) for num in input().split(", ") ]
result = 1 

for number  in numbers_list: 
    if number <= 5: 
        result *= number 
    elif number <= 10: 
        result /= number 

if type(result) == float and float.is_integer(result):
    print(int(result))
else:
    print(result)
