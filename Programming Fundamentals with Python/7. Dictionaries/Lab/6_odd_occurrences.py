data = input().split()

words = {}
for word in data:
    word = word.lower()
    if word not in words:
        words[word] = 0
    words[word] += 1
[print(key, end=" ") for key, value in words.items() if value % 2 != 0]
