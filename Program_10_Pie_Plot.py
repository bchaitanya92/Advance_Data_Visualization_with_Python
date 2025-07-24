import matplotlib.pyplot as plt  # Import library for plotting

# Data for the pie chart
countries = ['Brazil', 'Germany', 'Italy', 'Argentina', 'Hungary', 'France', 'England', 'Spain']
wins = [5, 4, 4, 3, 2, 2, 1, 1]
colors = ['y', 'g', 'b', 'r']  # Colors for the pie slices

# Create the pie chart
plt.pie(wins,  # Data for the pie slices
        labels=countries,  # Labels for the slices
        autopct="%1.1f%%",  # Display percentage values on the slices
        colors=colors,  # Set colors for the slices
        startangle=90,  # Rotate the pie chart by 90 degrees
        explode=[0.2] * len(countries),  # Separate the slices for better visibility
        shadow=True)  # Add a shadow effect

# Add a title to the pie chart
plt.title('FIFA World Cup Wins')

# Display the pie chart
plt.show()
