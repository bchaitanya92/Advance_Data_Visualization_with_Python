# Import the difflib library
import difflib

# Define a function to calculate the similarity between two strings
def string_similarity(str1, str2):
  """
  This function calculates the similarity between two strings using the difflib library.
  - It first converts both strings to lowercase for case-insensitive comparison.
  - Then, it uses the SequenceMatcher object from difflib to compare the two strings.
  - The ratio() method of the SequenceMatcher returns a float between 0 and 1,
    where 1 indicates identical strings and 0 indicates no similarity.
  """
  result = difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
  return result.ratio()

# Get the first string from the user
str1 = input("Enter first string: ")

# Get the second string from the user
str2 = input("Enter second string: ")

# Print the original strings
print("Original Strings:")
print(f"- String 1: {str1}")
print(f"- String 2: {str2}")

# Calculate and print the similarity score
similarity_score = string_similarity(str1, str2)
print(f"Similarity between the two strings: {similarity_score:.2f}")
