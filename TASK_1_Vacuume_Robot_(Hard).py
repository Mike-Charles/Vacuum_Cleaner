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
    print()
    
    for key, value in room.items():
        print(key, ":", value)
    print("-" * 20)
    print()

    if room['RoomA'] == "Clean" and room['RoomB'] == "Clean":
        print("All rooms are now clean!")
        print()
        print()
        break