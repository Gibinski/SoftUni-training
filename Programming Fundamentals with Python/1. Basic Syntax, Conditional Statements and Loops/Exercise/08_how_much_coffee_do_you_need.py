coffees = input()
count = 0
while coffees != "END":
    if coffees.lower() == "coding" or coffees.lower() == "dog" \
            or coffees.lower() == "cat" or coffees.lower() == "movie" :
        if coffees.islower():
            count += 1
        else:
            count += 2
    coffees = input()

if count > 5:
    print("You need extra sleep")
else:
    print(count)

