from os import remove, path

file_path = path.join("my_first_file.txt")

try:
    remove(file_path)
except FileNotFoundError:
    print('File already deleted!')