from re import findall
from os import path, linesep

words_list = []
words_dict = {}
pattern = r"[a-zA-Z\']+"


file_path_text = path.join("text2.txt")
with open(file_path_text, "r") as file:
    words_dict = {word.lower(): 0 for word in file.read().split()}

file_path_words = path.join("words.txt")
with open(file_path_words, "r") as file:
    words_list = findall(pattern, file.read())

for word in words_list:
    word = word.lower()
    if word in words_dict:
        words_dict[word] += 1

sorted_dict = dict(sorted(words_dict.items(), key=lambda x: x[1], reverse=True))

file_path_other = path.join("other.txt")
with open(file_path_other, "w") as file:
    for key, val in sorted_dict.items():
        line = f"{key} - {val}" + "\n"
        file.write(line)
