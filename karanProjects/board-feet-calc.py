print("Welcome to the board feet calculator!")

boardLength = float(input("Length of board in feet? "))
boardWidth = float(input("Width of board in inches? "))
boardThickness = float(input("Thickness of board in inches? "))
numberOfBoards = float(input("Number of boards to purchase? "))
pricePerBoardFoot = float(input("Price per board foot without dollar sign? "))

boardFeet = boardLength * boardWidth * boardThickness / 12

boardFeetResult = numberOfBoards * boardFeet

totalPrice = pricePerBoardFoot * boardFeetResult

print(f"The total cost for {boardFeetResult} is ${totalPrice}")