import matplotlib.pyplot as plt  # Import library for plotting
import numpy as np               # Import library for numerical computations

# Generate evenly spaced values from 1 to 20 with 10 elements
X = np.linspace(1, 20, 10)
print(X)  # Optional: Display the generated X values

# Calculate the square of X
Y1 = np.square(X)
print(Y1)  # Optional: Display the values of Y1

# Create the line plot with custom styling
plt.plot(X, Y1,
        marker='X',  # Use X markers
        linestyle='dashed',  # Use dashed line style
        color='r',  # Set line color to red
        linewidth=2,  # Set line width to 2
        markerfacecolor='b',  # Set marker face color to blue
        markersize=8)  # Set marker size to 8

# Add title, labels, and grid to the plot
plt.title('Line Plot of X^2')  # Set the title
plt.xlabel('Numbers')  # Set the x-axis label
plt.ylabel('Square')  # Set the y-axis label (corrected from 'Square Root')
plt.grid()  # Add gridlines to the plot

# Display the plot
plt.show()
