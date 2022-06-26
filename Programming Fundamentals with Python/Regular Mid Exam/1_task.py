cities_numbers = int(input())
total_profit = .0
for city in range(1, cities_numbers + 1):
    city_name = input()
    erned_money = float(input())
    expences = float(input())
    profit = .0
    if city % 5 == 0:
        profit = erned_money * 0.9 - expences
    elif city % 3 == 0:
        profit = erned_money - expences * 1.5
    else:
        profit = erned_money - expences
    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")
    total_profit += profit
print(f"Burger Bus total profit: {total_profit:.2f} leva.")