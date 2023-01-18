number = int(input())
rooms = [input().split() for i in range(number)]
def chairs_int(rooms):
    x = len(rooms[0]) 
    ch = int(rooms[1]) 
    return [x, ch]

def left_chairs(rooms):
    chairs_left = True
    x = 0
    ch = 0
    for room in rooms:
        x += room[0]
        ch += room[1]
        if room[0] < room[1]:
            chairs_left = False     
            print(f"{room[1] - room[0]} more chairs needed in room {rooms.index(room) + 1}")
    if chairs_left:
        print(f"Game On, {x - ch} free chairs left")


int_list = list(map(chairs_int, rooms))
left_chairs(int_list)