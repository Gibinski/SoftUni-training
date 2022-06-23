single_string = input().split(", ")
names = sorted(single_string, key=lambda item: (-len(item), item))
print(names)
