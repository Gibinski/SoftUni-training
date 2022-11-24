from os import path
from string import punctuation

output_file = open(path.join('02_output.txt'), "w")

file_patt = path.join('02_text.txt')
with open(file_patt, "r") as file:
    text = file.readlines()

for i in range(len(text)): 
    line = text[i]

    letters = 0
    marks = 0

    for symbol in line:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {i+1}: {''.join(line[:-1])} ({letters}) ({marks})\n")
output_file.close()
