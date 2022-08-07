data = input()

letters = {}
symbols = "".join(s for s in data.split())

for ch in symbols:
    if ch not in letters:
        letters[ch] = 0
    letters[ch] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")