def tax_func(car_type, km, years, type_c, declines, km_p, increase):
    km_tax = (km // km_p) * increase
    total_tax_to_pay = type_c - years * declines + km_tax
    print(f"A {car_type} car will pay {total_tax_to_pay:.2f} euros in taxes.")
    return total_tax_to_pay


vehicles_taxed = input().split(">>")
total_tax_collected = .0
for vehicle in vehicles_taxed:
    car = vehicle.split()
    car_type = car[0]
    years = int(car[1])
    km = int(car[2])
    if car_type == "family":
        total_tax_collected += tax_func(car_type, km, years, 50, 5, 3000, 12)
    elif car_type == "heavyDuty":
        total_tax_collected += tax_func(car_type, km, years, 80, 8, 9000, 14)
    elif car_type == "sports":
        total_tax_collected += tax_func(car_type, km, years, 100, 9, 2000, 18)
    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")