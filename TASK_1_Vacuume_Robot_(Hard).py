import random

room = {
    'RoomA': 'Dirty',
    'RoomB': 'Clean'
}

CurreLocation = random.choice(list(room.keys()))
steps = 10  
for _ in range(steps):
    print(f"Vaccume Robot in {CurreLocation}")
    if room[CurreLocation] == 'Dirty':
        print(f"{CurreLocation} is Dirty")
        print(f"Cleaning {CurreLocation}...")
        room[CurreLocation] = 'Clean'
    else:
        print(f"{CurreLocation} is already clean.")
    
    NewLocation = random.choice(list(room.keys()))
    while NewLocation == CurreLocation:
        NewLocation = random.choice(list(room.keys()))

    print(f"Now checking {NewLocation}, It is {room[NewLocation]}")
    CurreLocation = NewLocation

    print("Updated room state:", room)
    print("-" * 20)

    if room['RoomA'] == "Clean" and room['RoomB'] == "Clean":
        print("All rooms are now clean!")
        break
