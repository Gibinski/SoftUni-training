"""
Write a program that reads different floating-point numbers from the console. 
When it receives a number between 1 and 100 inclusive, the program should stop reading 
and should print "The number {number} is between 1 and 100".
"""

number = float(input())
while number < 1 or number > 100:
    number = float(input())

print(f"The number {number} is between 1 and 100")
