n = int(input())

set_even = set()
set_odd = set()
result = set()

for i in range(n):
    sum_char = sum(map(ord, input())) // (i + 1)
    if sum_char % 2 == 0:
        set_even.add(sum_char)
    else:
        set_odd.add(sum_char)

sum_even = sum(set_even)
sum_odd = sum(set_odd)

if sum_even > sum_odd:
    result = set_odd ^ set_even
elif sum_odd > sum_even:
    result = set_odd - set_even
else:
    result = set_even | set_odd

print(", ".join(map(str, result)))