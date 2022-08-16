line = input()
records = {}

while line != "Results":
    line = line.split(":")
    if line[0] == "Add":
        command, name, healt, energy = line
        if name not in records:
            records[name] = [int(healt), int(energy)]
        else:
            records[name][0] += int(healt)
    elif line[0] == "Attack": 
        if line[1] in records and line[2] in records:
            records[line[2]][0] -= int(line[3])
            records[line[1]][1] -= 1
            if records[line[2]][0] <= 0:
                print(f"{line[2]} was disqualified!")
                del records[line[2]]
            if records[line[1]][1] == 0:
                print(f"{line[1]} was disqualified!")
                del records[line[1]]         
    elif line[0] == "Delete":
        if line[1] == "All":
            records.clear()
        else:
            del records[line[1]]
    line = input()

print(f"People count: {len(records)}")
for persone, value in records.items():
    print(f"{persone} - {value[0]} - {value[1]}")
