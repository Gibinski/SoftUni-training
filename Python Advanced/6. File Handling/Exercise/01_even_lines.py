from os import path

symbols = ["-", ",", ".", "!", "?"]

file_path = path.join("01_text.txt")
with open(file_path, "r") as file:
    text = file.readlines() 

for line in range(0, len(text), 2):
    for symbol in symbols:
        text[line] = text[line].replace(symbol, "@")
    print()
    print(*text[line].split()[::-1], sep=" ")
