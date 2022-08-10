def print_materials(items):
    for material, quantity in items.items():
        print(f"{material}: {quantity}")


legendary = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
junks = {}

while True:
    line = input().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1].lower()
        if material in legendary_items:
            legendary_items[material] += quantity
            if legendary_items[material] >= 250:
                print(f"{legendary[material]} obtained!")
                legendary_items[material] -= 250
                break
        else:
            if material not in junks:
                junks[material] = 0
            junks[material] += quantity
    else:
        continue    
    break

print_materials(legendary_items)
print_materials(junks)