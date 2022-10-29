from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")

products = deque([])
product = input()
while product != "End":
    products.append(product)
    product = input()

robots = deque([])
busy_robots = []
for element in data:
    robot = {}
    name, processing_time = element.split("-")
    robot["name"] = name
    robot["processing_time"] = int(processing_time)
    robot["free"] = True
    robot["available_at"] = time
    robots.append(robot)

while products:           
    time = time + timedelta(seconds=1)
    curent_product = products.popleft()

    for robot in busy_robots:
        if robot["available_at"] == time:
            robots.append(robot)
            busy_robots.remove(robot)

    if robots:
            curent_robot = robots.popleft()
            curent_robot["available_at"] = time + timedelta(seconds=curent_robot["processing_time"])
            print(f'{curent_robot["name"]} - {curent_product} [{time.hour:02}:{time.minute:02}:{time.second:02}]')
            busy_robots.append(curent_robot)
    else:
        products.append(curent_product)



