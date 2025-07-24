# Get the first test mark from the user and convert it to a float
test1 = float(input("Enter the first test marks: "))

# Get the second test mark from the user and convert it to a float
test2 = float(input("Enter the second test marks: "))

# Get the third test mark from the user and convert it to a float
test3 = float(input("Enter the third test marks: "))

# Create an empty list to store the marks
marks = []

# Add the individual test marks to the list
marks.append(test1)
marks.append(test2)
marks.append(test3)

# Print the original list of marks
print("Original marks:", marks)

# Sort the list of marks in descending order (highest to lowest)
marks.sort(reverse=True)

# Print the sorted list of marks
print("Marks after sorting:")
print(marks)

# Calculate the average of the top two marks
average = (marks[0] + marks[1]) / 2

# Print the average marks
print("The average marks of the student is", average)
