text = input()

while True:
    try:
        num = int(input("Please enter a number: "))
        print(text * num)
        break
    except ValueError:
        print("Variable times must be an integer")
