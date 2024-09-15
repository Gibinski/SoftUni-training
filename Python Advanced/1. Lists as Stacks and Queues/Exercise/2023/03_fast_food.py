from collections import deque

quantity = int(input())

orders = deque(map(int, input().split()))

print(max(orders))

while orders:    
    if quantity >= orders[0]:
        quantity -= orders.popleft()
    else:
        result = ""
        while orders:
            result += str(orders.popleft()) + " "
        print(f"Orders left: {result}")
        break
else:
    print("Orders complete")
