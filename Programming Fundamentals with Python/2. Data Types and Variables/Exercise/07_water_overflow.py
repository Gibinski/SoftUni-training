lines = int(input())
capacity = 255
fules = 0
for lines in range(lines):
    liters = int(input())
    if fules + liters <= capacity:
        fules += liters
    else:
        print("Insufficient capacity!")
print(fules)
