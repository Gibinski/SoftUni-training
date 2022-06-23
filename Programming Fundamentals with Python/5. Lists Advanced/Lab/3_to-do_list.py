notes = [0] * 10

while True:
    comand = input()
    if comand == "End":
        break
    tokens = comand.split("-")
    priority = int(tokens[0])
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)
result = [element for element in notes if element != 0]
print(result)