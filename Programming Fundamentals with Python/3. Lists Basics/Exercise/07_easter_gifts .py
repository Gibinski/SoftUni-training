gifts = input().split()
commands = input()

while commands != "No Money":
    command = commands.split()
    if command[0] == "OutOfStock": 
        while command[1] in gifts:
            gifts[gifts.index(command[1])] = None
    elif command[0] == "Required" and int(command[2]) <= len(gifts) - 1:
        gifts[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        gifts.pop()
        gifts.append(command[1])
    commands = input()
gifts = [gift for gift in gifts if gift != None]
print(" ".join(gifts))