# Using comprehension, write a program that receives some text, 
# separated by space, and take only those words whose length is even. 
# Print each word on a new line.

[print(w) for w in input().split() if len(w) % 2 == 0]