"""
On the first line, you will be given a positive number, which will serve as a divisor. 
On the second line, you will receive a positive number that will be the boundary. 
You should find the largest integer N, that is:
divisible by the given divisor
less than or equal to the given bound
greater than 0
Note: it is guaranteed that N is found.
"""

divisor = int(input())
boundary = int(input())

# The exercise is about conditions and loops
largest_number = 0
for num in range(boundary, divisor, -1):
    if num % divisor == 0:
        largest_number = num
        break
    
# largest_number = (boundary // divisor) * divisor
print(largest_number)
