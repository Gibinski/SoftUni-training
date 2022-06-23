wagons = [0] * int(input())
commands = input()

while commands != "End":
    command = commands.split()
    if command[0] == "add":
        wagons[-1] += int(command[1])
    elif command[0] == "insert":
        wagons[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        wagons[int(command[1])] -= int(command[2])
    commands = input()

print(wagons)        