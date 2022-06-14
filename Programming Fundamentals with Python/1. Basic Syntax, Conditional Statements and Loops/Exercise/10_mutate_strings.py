# You will be given two strings. 
# Transform the first string into the second one, letter by letter, starting from the first one. 
# After each interaction, print the resulting string only if it is unique.

# Note: the strings will have the same length.

firs_str = input()
second_str = input()
previous_str = firs_str
result = ""
for i in range(len(firs_str)):
    left_part = second_str[:i + 1]
    right_part = firs_str[i + 1:]

    result = left_part + right_part
    if result == previous_str:
        continue
    previous_str = result
    print(result)
    