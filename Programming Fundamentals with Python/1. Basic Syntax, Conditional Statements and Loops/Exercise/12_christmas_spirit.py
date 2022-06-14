quantity = int(input())
days_left = int(input())

spirit = 0
budget = 0
if days_left % 10 == 0:
    spirit -= 30

for day in range(1, days_left + 1):
    if day % 10 == 0:
        spirit -= 20
        budget += 23
    elif day % 10 == 1:
        quantity += 2

    if day % 2 == 0:
        spirit += 5
        budget += 2 * quantity
    if day % 3 == 0:
        spirit += 13
        budget += 8 * quantity
    if day % 5 == 0:
        spirit += 17
        budget += 15 * quantity
        if day % 3 == 0:
            spirit += 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")