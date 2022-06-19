fires_cells  = input().split("#")
water = int(input())
cells = []
total_fire = 0

for cell in fires_cells:
    cells.append(cell.split(" = ")) 
print("Cells:")
for cell in cells:
    type_of_fire = cell[0]
    range = int(cell[1])
    filter_cell = (
        water >= range and (
        (type_of_fire == "High" and 81 <= range <= 125) or 
        (type_of_fire == "Medium" and 51 <= range <= 80) or 
        (type_of_fire == "Low" and 1 <= range <= 50)  
        )
    )
    if filter_cell:
        water -= range
        total_fire += range
        print(f" - {range}")
print(f"Effort: {(total_fire * 0.25):.2f}")
print(f"Total Fire: {total_fire}")