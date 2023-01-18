name = input()

line = input()
while line != "Registration":
    key, *value = line.split()
    if key == "Letters":
        if value[0] == "Lower":
            name = name.lower()
        elif value[0] == "Upper":
            name = name.upper()
        print(name)
    elif key == "Reverse":
        if 0 >= int(value[0]) and 0 >= int(value[1]) and int(value[1]) <= len(name):
            result = name[int(value[0]):int(value[1])+1]
            print(result[::-1])
    elif key == "Substring":
        if value[0] in name:
            name = name.replace(value[0] ,"")
            print(name)
        else:
            print(f"The username {name} doesn't contain {value[0]}.")
    elif key == "Replace":
        for ch in value[0]:
            if ch in name:
                name = name.replace(ch, "-")
        print(name)
    elif key == "IsValid":
        if value[0] in name:
            print("Valid username.")
        else:
            print(f"{value[0]} must be contained in your username.")
    line = input()