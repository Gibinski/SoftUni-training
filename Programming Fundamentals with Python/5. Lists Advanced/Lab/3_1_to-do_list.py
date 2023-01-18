notes = [] 
while True:
    tokens = input().split("-")
    if tokens[0] == "End":
        break
    priority = int(tokens[0])
    note = tokens[1]
    notes.append((priority, note))
result = [element[1] for element in sorted(notes)]
print(result)