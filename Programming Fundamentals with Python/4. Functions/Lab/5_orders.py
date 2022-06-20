def orders(product, quantity):
    order = {"coffee": 1.5, "coke": 1.4, "water": 1.0, "snacks": 2.0}
    result  = order[product] * quantity
    return f"{result:.2f}"

product = input()
quabtity = float(input())
print(orders(product, quabtity))