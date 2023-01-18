from collections import deque

people = deque()
line = input()
while line != "End":
    if line == "Paid":
        print("\n".join(people))
        people.clear()
    else:
        people.append(line)
    line = input()
print(f"{len(people)} people remaining.")