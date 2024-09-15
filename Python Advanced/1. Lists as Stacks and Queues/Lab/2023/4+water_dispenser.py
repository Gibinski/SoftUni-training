from collections import deque

people = deque()
dispenser = int(input())

while True:
    line = input()
    if line == "Start":
        break
    people.append(line)

while True:
    line = input()
    if line == "End":
        break

    if " " in line:
        dispenser += int(line.split()[1]) 
    else:
        liters = int(line) 
        if dispenser >= liters:
            print(f"{people.popleft()} got water")
            dispenser -= liters
        else:
            print(f"{people.popleft()} must wait")
print(f"{dispenser} liters left")
