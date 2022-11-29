from os import remove

while True:
    # input is in file 03_input.txt
    info = input().split("-")

    if info[0] == "End":
        break

    elif info[0] == "Create":
        file = open(info[1], "w")
        file.close()

    elif info[0] == "Add":
        with open(info[1], "a") as file:
            file.write(info[2] + "\n")

    elif info[0] == "Replace":
        try:
            with open(info[0], "r+") as file:
                text = file.readlines()

                for i in range(len(text)):
                    text[i] = text[i].replace(info[2], info[3])
        except FileNotFoundError:
            print("An error occurred")

    elif info[0] == "Delete":
        try:
            remove(info[1])
        except FileNotFoundError:
            print("An error occurred")
