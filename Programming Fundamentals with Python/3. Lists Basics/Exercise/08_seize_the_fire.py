fires_cells  = input().split("#")
water = int(input())
total_fire = 0

print("Cells:")
for cell in fires_cells:
    cells = cell.split(" = ") 
    type_of_fire = cells[0]
    range = int(cells[1])
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