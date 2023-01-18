import re

pattern = r"(w{3}\.[A-Za-z0-9\-]+(\.[a-z]+)+)"
text = input()
while text:
    matches = re.search(pattern, text)
    if matches:
        print(matches.groups(0)[0])
    text = input()

