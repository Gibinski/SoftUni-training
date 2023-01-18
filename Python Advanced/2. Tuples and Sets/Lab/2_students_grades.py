n = int(input())

grades = {}

for _ in range(n):
    name, grade_as_str = input().split()
    grade = float(grade_as_str)
    if name not in grades: 
        grades[name] = []
    grades[name].append(grade)

for name, grade in grades.items():   
    print(f"{name} -> {' '.join([f'{el:.2f}' for el in grade])} (avg: {(sum(grade) / len(grade)):.2f})")
    