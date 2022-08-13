import re

pattern = r"\b[A-Z][a-z]+ \b[A-Z][a-z]+\b"
name = input()
valid_name = re.findall(pattern, name)

print(*valid_name)
