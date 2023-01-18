file_path = r".\text.txt"

try:
    file = open(file_path, "r")
    print("File foung")
except FileNotFoundError:
    print(f"{file} does not exist")