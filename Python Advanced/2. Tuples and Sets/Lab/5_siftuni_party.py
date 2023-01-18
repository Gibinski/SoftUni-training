n = int(input())
guests = set()

for _ in range(n):
    guests.add(input())

guests_code = input()    
while guests_code != "END":    
    guests.remove(guests_code)
    guests_code = input()

print(len(guests))
print('\n'.join(sorted(guests)))
