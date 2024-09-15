from collections import deque
from datetime import datetime, timedelta

robots = input().split(";")
for i in range(len(robots)):
    robot = robots[i].split("-")
    robots[i] = {
        "name": robot[0],
        "processing_time": int(robot[1]),
        "available_at": 0
    }

start_time = datetime.strptime(input(), "%H:%M:%S")

item = deque([])
next_item = input()
while next_item != "End":
    item.append(next_item)
    next_item = input()

current_time = 0

while item:           
    current_time += 1 
    current_item = item.popleft()

    for robot in robots:
        if robot["available_at"] <= current_time:
            robot["available_at"] = current_time + robot["processing_time"]
            time = (start_time + timedelta(seconds=current_time)).strftime("%H:%M:%S")
            print(f"{robot['name']} - {current_item} [{time}]")

            break
    else:
        item.append(current_item)



