import matplotlib.pyplot as plt  # Import library for plotting
import numpy as np               # Import library for numerical computations
import seaborn as sns            # Import library for advanced plotting

def sinplot(n=10):  # Define a function to create a plot of multiple sine waves
    x = np.linspace(0, 14, 100)  # Generate evenly spaced values for x-axis
    for i in range(1, n + 1):  # Loop through each wave
        plt.plot(x, np.sin(x + i * 0.5) * (n + 2 - i))  # Plot each sine wave with varying amplitude

# Set Seaborn theme for aesthetics
#sns.set()
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})

# Generate the plot
sinplot()

# Add title and display
plt.title('Seaborn Plots with Aesthetic Functions')
plt.show()
