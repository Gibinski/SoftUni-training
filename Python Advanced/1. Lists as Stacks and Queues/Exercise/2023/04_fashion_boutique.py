clothes = list(map(int, input().split()))
capacity = int(input())
counter = 1
remaining_of_capacity = capacity

while clothes:
    if remaining_of_capacity >= clothes[-1]:
        remaining_of_capacity -= clothes.pop()
    else:
        remaining_of_capacity = capacity
        counter += 1
print(counter)