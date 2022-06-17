numbers_of_strings = int(input())
word = input()
strings = []
new_strings = []
for i in range(numbers_of_strings):
    strings.append(input())
    if word in strings[i]:
        new_strings.append(strings[i])

print(strings)
print(new_strings)