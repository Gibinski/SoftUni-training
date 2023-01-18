legendary = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
items = {"shards": 0, "fragments": 0, "motes": 0}

while True:
    line = input().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1].lower()
        if material not in items:
            items[material] = 0

        items[material] += quantity

        if (items[material] >= 250) and (material in legendary.keys()):
            print(f"{legendary[material]} obtained!")
            items[material] -= 250
            break
    else:
        continue    
    break
for material, quantity in items.items():
    print(f"{material}: {quantity}")
