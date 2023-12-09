from collections import deque

monsters = deque([int(n) for n in input().split(",")])
soldiers = [int(n) for n in input().split(",")]

monsters_in_the_begining = len(monsters)
while monsters and soldiers:
    soldier = soldiers.pop()
    monster = monsters.popleft()
    if soldier >= monster:
        
        soldier -= monster
        if not soldiers and soldier > 0:
            soldiers.append(soldier)
        elif soldiers:
            soldiers[-1] += soldier
    else:
        monster -= soldier
        monsters.append(monster)


if not monsters:
    print("All monsters have been killed!")
if not soldiers:
    print("The soldier has been defeated.")

killed_monsters = monsters_in_the_begining - len(monsters)
print(f"Total monsters killed: {killed_monsters}")
            