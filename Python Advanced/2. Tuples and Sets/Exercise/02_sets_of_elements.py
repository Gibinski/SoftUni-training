n, m = tuple(int(el) for el in input().split())

set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(input())

for _ in range(m):
    set_m.add(input())

print("\n".join(set_m & set_n))
