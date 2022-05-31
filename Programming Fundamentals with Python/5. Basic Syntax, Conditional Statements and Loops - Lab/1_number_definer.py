"""Write a program that reads a floating-point number and:
prints "zero" if the number is zero
prints "positive" or "negative"
adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds 
1 000 000"""


number = float(input())

abs_num = abs(number)
if abs_num > 0:
    if abs_num < 1:
        print("small", end=" ")
    elif abs_num > 10 ** 6:
        print("large", end=" ")

    if number < 0:
        print("negative")
    else:
        print("positive")
else:
    print("zero")