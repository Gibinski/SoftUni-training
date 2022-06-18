numbers = input().split()
n = int(input())
list_of_integer = [int(i) for i in numbers]
sorted_list = list_of_integer.copy()
sorted_list.sort()
numbers_to_remove = sorted_list[:n]
for num in numbers_to_remove:
    list_of_integer.remove(num)
print(", ".join(str(num) for num in list_of_integer))