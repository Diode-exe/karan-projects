import math

print("Welcome to the tile cost calculator!")

try: 
    lengthOfRoom = int(input("Length of room in ft? "))
    widthOfRoom = int(input("Width of room in ft? "))
    lengthOfTile = int(input("Length of tile in ft? "))
    widthOfTile = int(input("Width of tile in ft? "))
except ValueError:
    print("One or more values was invalid! Numbers only, please")
    exit()

widthOfRoomByTile = math.ceil(widthOfRoom / widthOfTile)
print(f"Tiles in width of room: {widthOfRoomByTile}")

lengthOfRoomByTile = math.ceil(lengthOfRoom / lengthOfTile)
print(f"Tiles in length of room: {lengthOfRoomByTile}")

exit() if input("Continue to calculate cost? y or n: ").lower() != "y" else None

costOfTile = float(input("Cost of each tile in dollars? "))

areaOfTileInRoom = lengthOfRoomByTile * widthOfRoomByTile

priceOfAreaInRoom = areaOfTileInRoom * costOfTile

print(f"Tiling the room will cost {priceOfAreaInRoom} dollars to tile")