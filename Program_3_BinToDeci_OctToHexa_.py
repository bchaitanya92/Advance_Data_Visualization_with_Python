# Function to convert a binary number to its decimal equivalent
def BinToDeci(binary):
  """
  This function takes a binary string as input and returns its decimal equivalent.
  - It uses the built-in `int` function with base 2 to directly convert the string.
  """
  return int(binary, 2)

# Function to convert an octal number to its hexadecimal equivalent
def OctToHex(octal):
  """
  This function takes an octal string as input and returns its hexadecimal equivalent.
  - It first converts the octal string to its decimal equivalent using `int` with base 8.
  - Then, it uses the built-in `hex` function to convert the decimal value to hexadecimal.
  - Additionally, it prints the decimal equivalent before returning the hexadecimal value.
  """
  decimal_value = int(octal, 8)
  print(f"Decimal Equivalent: {decimal_value}")
  return hex(decimal_value)

# Get user input for a binary number
binary_number = input("Enter a Binary No. : ")

# Convert the binary number to decimal and store the result
decimal_number = BinToDeci(binary_number)

# Print the decimal equivalent of the binary number
print(f"Decimal Equivalent: {decimal_number}")

# Get user input for an octal number
octal_number = input("Enter an Octal No. : ")

# Convert the octal number to hexadecimal and store the result
hexadecimal_number = OctToHex(octal_number)

# Print the hexadecimal equivalent of the octal number
print(f"HexaDecimal Equivalent: {hexadecimal_number}")
