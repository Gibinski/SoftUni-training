n = int(input())

elements = set()

for _ in range(n):
    new_el = input().split()
    elements.update(new_el)

print("\n".join(elements))