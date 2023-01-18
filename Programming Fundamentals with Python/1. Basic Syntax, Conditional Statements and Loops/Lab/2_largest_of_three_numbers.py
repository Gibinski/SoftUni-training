"""Write a program that receives three whole numbers and prints the largest one."""

largest_number = int(input())
for i in range(2):
    number = int(input())
    if largest_number < number:
        largest_number = number

print(largest_number)
