toConvert = input("Enter a number (binary or decimal): ")

# Try binary → decimal
try:
    convertedToDecimal = int(toConvert, 2)
    print(f"{toConvert} in decimal is {convertedToDecimal}")
except ValueError:
    print(f"{toConvert} is not a valid binary number.")

# Try decimal → binary
try:
    decimal_number = int(toConvert)  # convert string to int (decimal)
    convertedToBinary = bin(decimal_number)[2:]  # remove '0b'
    print(f"{toConvert} in binary is {convertedToBinary}")
except ValueError:
    print(f"{toConvert} is not a valid decimal number.")
