snowballs = int(input())
max_weight = 0
max_time = 1
max_quality = 0
max_value = 0
for ball in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight // time) ** quality
    if value > max_value:
        max_weight = weight
        max_time = time
        max_quality = quality
        max_value = value

print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")
