number = int(input())

for i in range(number):
    string = input()
    for char in enumerate(string):
        if char == "," or char == "." or char == "_":
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")


