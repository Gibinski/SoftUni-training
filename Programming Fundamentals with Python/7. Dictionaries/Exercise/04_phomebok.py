line = input()
phonebok = {}
while True:
    if "-" not in line:
        break
    name, number = line.split("-")
    phonebok[name] = number
    line = input()

for _ in range(int(line)):
    name = input()
    if name in phonebok:
        print(f"{name} -> {phonebok[name]}")
    else:
        print(f"Contact {name} does not exist.")