lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmet_brakes = lost_fights_count // 2  
total_sword_brakes = lost_fights_count // 3 
total_shield_brakes = lost_fights_count // 6 
total_armor_brakes = total_shield_brakes // 2
aureus = total_helmet_brakes * helmet_price + \
    total_sword_brakes * sword_price + \
    total_shield_brakes * shield_price + \
    total_armor_brakes * armor_price

print(f"Gladiator expenses: {aureus:.2f} aureus")  
