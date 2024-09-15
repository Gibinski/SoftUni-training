stack = []
n = int(input())

for i in range(n):
    date = input().split()
    query_type = date[0]

    if query_type == "1":
        number = int(date[1])
        stack.append(number) 
    elif query_type == "2":
        if stack:
            stack.pop() 
    elif query_type == "3":
        if stack:
            print(max(stack)) 
    else: 
        if stack:
            print(min(stack)) 

print(*stack[::-1], sep=", ")