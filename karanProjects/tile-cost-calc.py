import math

print("Welcome to the tile cost calculator!")

try: 
    lengthOfRoom = int(input("Length of room? "))
    widthOfRoom = int(input("Width of room? "))
    lengthOfTile = int(input("Length of tile? "))
    widthOfTile = int(input("Width of tile? "))
except ValueError:
    print("One or more values was invalid! Numbers only, please")
    exit()

widthOfRoomByTile = math.ceil(widthOfRoom / widthOfTile)
print(f"Tiles in width of room: {widthOfRoomByTile}")

lengthOfRoomByTile = math.ceil(lengthOfRoom / lengthOfTile)
print(f"Tiles in length of room: {lengthOfRoomByTile}")

exit() if input("Continue to calculate cost? y or n: ").lower() != "y" else None

costOfTile = float(input("Cost of each tile? "))

areaOfTileInRoom = lengthOfRoomByTile * widthOfRoomByTile

priceOfAreaInRoom = areaOfTileInRoom * costOfTile

print(f"Tiling the room will cost {priceOfAreaInRoom}")