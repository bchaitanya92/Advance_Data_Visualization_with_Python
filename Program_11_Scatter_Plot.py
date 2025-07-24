import matplotlib.pyplot as plt

# Define the list of country
countrys = ['Brazil', 'Russia', 'India', 'China', 'South Africa']

# Create an empty list to store user-input values
user_values = []

# Prompt the user for each country's Per_Capita_Income
for country in countrys:
  value = float(input(f"Enter Per_Capita_Income for {country}: "))
  user_values.append(value)

# Create the scatter chart
plt.scatter(countrys, user_values, s=150, c='c', linewidth=1,marker='D',edgecolor='k')


# Add labels and adjust font sizes
plt.xlabel("Country", fontsize=12)
plt.ylabel("Per_Capita_Income", fontsize=12)

# Add Title
plt.title("Per_Capita_Income of BRICS Nations.")

# Display the plot
plt.show()
