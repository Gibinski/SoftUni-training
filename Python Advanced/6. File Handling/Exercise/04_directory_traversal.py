import os

directory = input()
extensions = {}
result = []

for file_name in os.listdir(directory):
    file = os.path.join(directory, file_name)

    if os.path.isfile(file):
        extension = file_name.split(".")[-1]

        if extension not in extensions:
            extensions[extension] = []
        extensions[extension].append(file_name)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for ex, files in extensions:
    result.append(f'.{ex}')

    for file in files:
        result.append(f"- - - {file}")

with open("report.txt", "w") as file:
    file.write("".join(result))