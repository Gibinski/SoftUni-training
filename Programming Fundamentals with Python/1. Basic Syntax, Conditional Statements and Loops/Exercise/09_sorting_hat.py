name = input()

while name != "Welcome!":
    len_name = len(name)
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    else:
        if len_name < 5:
            print(f"{name} goes to Gryffindor.")
        elif len_name == 5:
            print(f"{name} goes to Slytherin.")
        elif len_name == 6:
            print(f"{name} goes to Ravenclaw.")
        else:
            print(f"{name} goes to Hufflepuff.")
    name = input()
else:
    print("Welcome to Hogwarts.")    


