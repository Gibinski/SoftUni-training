# You will be given two strings. Transform the first string into the second one, 
# letter by letter, starting from the first one. After each interaction, 
# print the resulting string only if it is unique.

# Note: the strings will have the same length.

firs_str = input()
second_str = input()
previous_str = firs_str

for i in range(len(firs_str)):
    right_part = firs_str[:i + 1]
    right_part = firs_str[i + 1:]

    if i is previous_char:

        continue
    firs_str[i] = second_str[i]
    print(firs_str)
    previous_char = firs_str[i]


