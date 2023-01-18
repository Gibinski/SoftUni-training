text = input().split()
new_text = []
for word in text:
    number = ""
    for i in range(len(word)):
        if word[i].isdigit():
            number += word[i]
        else:
            word = list(word)
            word[i], word[-1] = word[-1], word[i]
            new_word = chr(int(number)) + "".join([word[i] for i in range(i, len(word))]) 
            new_text.append(new_word)
            break
print(*new_text, sep=" ")