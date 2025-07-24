# Get the value from the user
value = input("Enter the value: ")

# Check if the number is a palindrome
if value == value[::-1]:
    print("The given number is a palindrome.")
else:
    print("The given number is not a palindrome.")

# Count occurrences of each digit in the number
for i in range(10):
    digit_count = value.count(str(i))
    if digit_count > 0:
        print(f"{str(i)} appears {digit_count} time(s).")
