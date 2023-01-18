import re

pattern = r">>([a-zA-Z]+)<<([0-9]+.?[0-9]*)!([0-9]+)"
text = input()
cost = .0
print("Bought furniture:")
while text != "Purchase":
    match = re.search(pattern, text)
    if match:
        name, price, quantity = match.groups()
        print(name)
        cost += float(price) * int(quantity)
    text = input()
print(f"Total money spend: {cost:.2f}")