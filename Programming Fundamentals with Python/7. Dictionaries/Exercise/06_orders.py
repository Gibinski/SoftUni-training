products = {}

data = input()
while data != "buy":
    name, price, quantity = data.split()
    if name not in products:
        products[name] = [0, 0]
    products[name][0] = float(price) 
    products[name][1] += int(quantity) 

    data = input()

for name, value in products.items():
    total_price = value[0] * value[1]
    print(f"{name} -> {total_price:.2f}")
    
