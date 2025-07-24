import matplotlib.pyplot as plt

# Define the list of days (constant)
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Create an empty list to store user-input values
user_values = []

# Prompt the user for each day's value
for day in days:
  value = float(input(f"Enter value for {day}: "))
  user_values.append(value)

# Create the bar chart
plt.bar(days, user_values, color='r', width=0.3)

# Add labels and adjust font sizes
plt.xlabel("Days", fontsize=12)
plt.ylabel("Tips", fontsize=12)

# Add Title
plt.title("Days v/s Tips")

# Display the plot
plt.show()
