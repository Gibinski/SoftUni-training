employees = input().split()
factor = int(input())

happy = list(map(lambda x: int(x) * factor, employees))
happy_employees = list(filter(lambda x: x >= sum(happy) / len(happy), happy))
happy_count = len(happy_employees)
total_count = len(happy)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
