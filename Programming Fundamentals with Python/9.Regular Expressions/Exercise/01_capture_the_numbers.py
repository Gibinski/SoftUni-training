import re

line = input()
while True:
    if line:
        matches = re.findall(r"\d+", line)
        if matches:
            print(" ".join(matches), end=" ")
        line = input()
    else:
        break
