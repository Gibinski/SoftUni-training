def str_range_to_set(set_value):
    set_start_value, set_end_value = tuple(set_value.split(","))
    return set(range(int(set_start_value), int(set_end_value) + 1))
    

n = int(input())

longest_intersection = set()
for i in range(n):
    set_1_value, set_2_value = tuple(input().split("-"))

    set_1 = str_range_to_set(set_1_value) 
    set_2 = str_range_to_set(set_2_value) 

    intersection = set_1 & set_2
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}")
