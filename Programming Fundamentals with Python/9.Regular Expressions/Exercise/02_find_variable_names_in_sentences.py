import re

pattern = r"\b_([A-Za-z0-9]+)\b"
text = input()
matches = re.findall(pattern, text)
print(",".join(matches))