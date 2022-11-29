from os import path, linesep

path_file = path.join("my_first_file.txt")
with open(path_file, "w") as file:
     file.write('I just created my first file!' + linesep)
