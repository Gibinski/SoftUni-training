line = input()
courses = {}

while ":" in line:
    name, id, course = line.split(":")
    if not course in courses:
        courses[course] = {}
    courses[course][id] = name
    line = input()
 
course = " ".join(line.split("_"))
for id, name in courses[course].items():
     print(f"{name} - {id}")
