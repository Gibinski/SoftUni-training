n = int(input())

parking = set()
for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parking.add(car_number)
    else:
        if car_number in parking:
            parking.remove(car_number)

for car in parking:
    print(car)
