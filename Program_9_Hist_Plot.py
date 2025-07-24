import matplotlib.pyplot as plt  # Import library for plotting
import numpy as np              # Import library for numerical computations
import random                   # Import library for random number generation

# Set a seed for reproducibility (optional, but recommended for consistent results)
np.random.seed(42)

# Generate 100 random student marks with a normal distribution, mean=70, standard deviation=15
student_marks = np.random.normal(loc=70, scale=15, size=100)

# Create a histogram of the student marks
plt.hist(student_marks,   # Data to plot
         bins=20,          # Number of bins in the histogram
         color='skyblue',  # Color of the bars
         edgecolor='black')  # Edge color of the bars

# Add labels and title to the plot
plt.xlabel('Student Marks')
plt.ylabel('Frequency')
plt.title('Distribution of Student Marks')

# Display the plot
plt.show()

# To change the font of labels and title:
# font={'family':'Algerian','color':'red','size':'42'}
