# Get the sentence from the user
str = input("Enter the sentence: ")

# Initialize variables to count words, digits, uppercase, lowercase letters
w,d,l,u=0,0,0,0

# Split the sentence into individual words using the "split()" method
words = str.split()

# Count the number of words
words = len(words)

# Loop through each character in the sentence
for i in str:
    # Check if the character is a digit
    if i.isdigit():
        d += 1
    # Check if the character is uppercase
    elif i.isupper():
        u += 1
    # Check if the character is lowercase
    elif i.islower():
        l += 1


# Print the counts for each category
print("Number of words: ",w)
print("Number of digits: ",d)
print("Number of uppercase letters: ",u)
print("Number of lowercase letters: ",l)