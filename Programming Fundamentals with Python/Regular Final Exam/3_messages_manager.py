capacity = int(input())
messages_manager = {}
line = input().split("=")
while line[0] != "Statistics":
    if line[0] == "Add":
        command, username, send, received = line
        if username not in messages_manager:
            messages_manager[username] = int(send) + int(received)
    elif line[0] == "Message":
        command, sender, receiver = line
        if sender in messages_manager.keys() and receiver in messages_manager.keys():
            messages_manager[sender] += 1
            messages_manager[receiver] += 1
            
            if messages_manager[sender] >= capacity:
                print(f"{sender} reached the capacity!")
                del messages_manager[sender]
            if messages_manager[receiver] >= capacity:
                print(f"{receiver} reached the capacity!")
                del messages_manager[receiver]
    elif line[0] == "Empty":
        cmmand, username = line
        if username == "All":
            messages_manager = {}
        else:
            messages_manager.pop(username)
    line = input().split("=")

print(f"Users count: {len(messages_manager)}")
for username, messages in messages_manager.items():
    print(f"{username} - {messages}")