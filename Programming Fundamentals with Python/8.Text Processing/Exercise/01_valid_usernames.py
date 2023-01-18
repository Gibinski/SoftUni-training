usernames = input().split(", ")

for name in usernames:
    if not 3 <= len(name) <= 16:
        continue
    if " " in name:
        continue
    for ch in name:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            break
    else:
        print(name)