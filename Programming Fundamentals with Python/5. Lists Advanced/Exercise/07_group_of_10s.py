groups_of_nums = [int(n) for n in input().split(", ")]
max_num = max(groups_of_nums)
groups_len = max_num // 10
if max_num % 10 != 0:
    groups_len += 1

for group in range(10, groups_len * 11, 10):
    list_of_numbers = []
    for num in groups_of_nums:
        if num <= group and num > group - 10:
            list_of_numbers.append(num)
    else:
        print(f"Group of {group}'s: {list_of_numbers}")
