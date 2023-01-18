import re

text = input()
pattern = r"(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
matches = re.finditer(pattern, text)
result = [match.group() for match in matches]
print(", ".join(result))
