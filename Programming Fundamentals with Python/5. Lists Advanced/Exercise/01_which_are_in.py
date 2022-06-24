first_string = input().split(", ")
second_string = input().split(", ")
substring = []
for word1 in first_string:
    for word2 in second_string:
        if word1 in word2 and not word1 in substring:
            substring.append(word1)
            break 
print(substring)