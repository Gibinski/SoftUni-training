from os import path

file_patt = path.join('02_text.txt')
with open(file_patt, "r") as file:
    text = file.readlines()


