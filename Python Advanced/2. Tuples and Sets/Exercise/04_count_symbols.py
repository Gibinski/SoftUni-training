tuple_text = tuple(input())
sorted_unique_chars = sorted(set(tuple_text))

for ch in sorted_unique_chars:
    print(f"{ch}: {tuple_text.count(ch)} time/s")