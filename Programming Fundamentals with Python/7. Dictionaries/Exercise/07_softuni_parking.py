num = int(input())
parking = {}

for _ in range(num):
    line = input().split() 
    command = line[0] 
    username = line[1] 
    if command == "register":
        license_plate_number = line[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif command == "unregister":
        if username in parking:
            print(f"{username} unregistered successfully")
            parking.pop(username)
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")