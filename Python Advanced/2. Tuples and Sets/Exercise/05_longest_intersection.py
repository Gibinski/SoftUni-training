n = int(input())

intersection = set()
longest_intersection = set()
for i in range(n):
    set_1_value, set_2_value = tuple(input().split("-"))

    set_1_start_value, set_1_end_value = tuple(set_1_value.split(","))
    set_1 = set(range(int(set_1_start_value), int(set_1_end_value) + 1))

    set_2_start_value, set_2_end_value = tuple(set_2_value.split(","))
    set_2 = set(range(int(set_2_start_value), int(set_2_end_value) + 1))

    intersection = set_1 & set_2
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection.copy()

print(f"Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}")
