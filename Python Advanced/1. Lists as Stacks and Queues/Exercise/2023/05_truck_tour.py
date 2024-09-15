from collections import deque

n = int(input())
petrol_pumps = deque([])

for _ in range(n):
    petrol, distance = input().split()
    petrol_pumps.append(int(petrol) - int(distance))

if_break = False
for i in range(n):
    tank = 0
    for j in petrol_pumps:
        tank += j
        if tank < 0:
            petrol_pumps.append(petrol_pumps.popleft())
            break
    else:
        print(i)
        break

