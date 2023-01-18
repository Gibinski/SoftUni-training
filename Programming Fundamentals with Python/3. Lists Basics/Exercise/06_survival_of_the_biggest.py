numbers = input().split()
n = int(input())
list_of_integer = [int(i) for i in numbers]
for _ in range(n):
    min_num = min(list_of_integer)
    list_of_integer.remove(min_num)
print(", ".join(str(num) for num in list_of_integer))