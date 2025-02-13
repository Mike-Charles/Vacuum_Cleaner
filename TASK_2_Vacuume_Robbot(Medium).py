import random
import time

rooms = {
    'Room 41': 'Dirty',
    'Room 42': 'Clean',
    'Room 43': 'Dirty', 
    'Room 44': 'Clean',
    'Room 45': 'Dirty',
    'Room 46': 'Clean',
    'Room 47': 'Dirty'
}

cleanTime = 2  
traveTime = 1 

curreLocation = random.choice(list(rooms.keys()))
steps = 20

def PrEnvironment():
    print()
    print("Updated Environment State:")
    for room, status in rooms.items():
        print(f"{room}: {status}")
    print("-" * 20)

for _ in range(steps):
    print(f"Vacuum Robot is in {curreLocation}")
    
    if rooms[curreLocation] == 'Dirty':
        print(f"{curreLocation} is Dirty. Cleaning...")
        rooms[curreLocation] = 'Clean'
    else:
        print(f"{curreLocation} is already clean.")
    
    if all(status == 'Clean' for status in rooms.values()):
        PrEnvironment()
        print()
        print("All rooms are now clean.")
        print()
        print()
        break
    
    roomkeys = list(rooms.keys())
    currentInd = roomkeys.index(curreLocation)
    
    if currentInd < len(roomkeys) - 1:
        newLoca = roomkeys[currentInd + 1]
    else:
        newLoca = roomkeys[0]  
    
    print(f"Moving to {newLoca}...") 
    curreLocation = newLoca
    
    PrEnvironment()
    print("\n")
