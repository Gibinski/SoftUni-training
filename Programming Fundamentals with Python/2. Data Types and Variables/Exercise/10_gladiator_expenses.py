lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
aureus = 0
shield_brakes_count = 0
for lost in range(1, lost_fights_count + 1):
    if lost % 2 == 0:
        aureus += helmet_price
    if lost % 3 == 0:
        aureus += sword_price
        if lost % 2 == 0:
            aureus += shield_price
            shield_brakes_count += 1
            if shield_brakes_count % 2 == 0:
                aureus += armor_price
print(f"Gladiator expenses: {aureus:.2f} aureus")  
