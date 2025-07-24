import matplotlib.pyplot as plt  # Import library for plotting
import numpy as np               # Import library for numerical computations

# Create evenly spaced values from 1 to 20, with 10 elements
X = np.linspace(1, 20, 10)
print(X)  # Optional: Display the generated X values

# Create three sets of Y values based on X
Y1 = X  # Y1 is the same as X
print(Y1)  # Optional: Display the values of Y1

Y2 = np.square(X)  # Y2 is the square of X
print(Y2)  # Optional: Display the values of Y2

Y3 = np.sqrt(X)  # Y3 is the square root of X
print(Y3)  # Optional: Display the values of Y3

# Create the line plot
plt.plot(X, Y1, 'r',X,Y2,'b',X,Y3,'g' )  # Plot Y1 with red color,Y2 with blue color, and Y3 with green color

"""
# Create the line plot with multiple lines
plt.plot(X, Y1, 'r', label='x')  # Plot Y1 with red color and label 'x'
plt.plot(X, Y2, 'b', label='x-Square')  # Plot Y2 with blue color and label 'x-Square'
plt.plot(X, Y3, 'g', label='Square Root')  # Plot Y3 with green color and label 'Square Root'

# Add labels and title
plt.legend(loc='center left')  # Place the legend on the center left
"""

# Add legends and title
plt.legend(['x','x-Square','Square Root'],loc='center left') #Y1 with label 'x',Y2 with label 'x-square',and Y3 with label 'square root'; place the legend on the center left
plt.title('Line Plot')  # Set the title of the plot

# Add grid and display the plot
plt.grid()  # Add gridlines to the plot
plt.show()  # Display the plot