from collections import deque

que = deque(input())
types = {
    ")": "(",
    "]": "[",
    "}": "{"
}

stack = []
if len(que) % 2 == 0:
    while que:
        bracket = que.popleft()
        if bracket in types.values():
            stack.append(bracket)
        else:
            if stack:
                if types[bracket] == stack[-1]:
                    stack.pop()       
                else:
                    print("NO")
                    break           
            else:
                print("NO")
                break           
    else:
        print("YES")
else:
    print("NO")
