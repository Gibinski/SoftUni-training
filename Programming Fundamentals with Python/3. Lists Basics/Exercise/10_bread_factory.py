energy = 100
coins = 100
days = []
working_day_events = input().split("|")
for day in working_day_events:
    days.append(day.split("-")) 

for day in days:
    event = day[0]
    value = int(day[1])
    if event == "rest":
        if energy + value > 100:
            value = 100 - energy
            energy = 100
        else:
            energy += value
        print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")