from cgitb import reset
import re 

def letters(text):
    result = ""
    for ch in text:
        if ch.isalnum():
            result += ch
    return result

pattern = r"^([a-zA-Z0-9@#\!\$\?]+)=(\d+)<<(\w+)"
line = input()

while line != "Last note":
    match = re.search(pattern, line)
    line = input()
    if match:
        name, length, code = match.groups()
        if len(code) <= int(length):
            nameOfMountain = letters(name)
            print(f"Coordinates found! {nameOfMountain} -> {code}")
            continue
    print("Nothing found!")

