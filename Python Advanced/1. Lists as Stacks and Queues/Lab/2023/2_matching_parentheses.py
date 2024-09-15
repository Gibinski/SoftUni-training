text = list(input())
stack = []

for i, ch in enumerate(text):
    if ch == "(":
        stack.append(i)
    elif ch == ")":
        print("".join(text[stack.pop(): i + 1]))
