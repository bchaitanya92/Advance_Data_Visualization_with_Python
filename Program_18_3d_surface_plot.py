# Import libraries for visualization and numerical computations
import plotly.graph_objects as go
import numpy as np

# --- Generate 3D data ---
# Create a grid of x and y values spanning -5 to 5 with 100 points each
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)  # Create a 2D grid from x and y

# Calculate z values based on the equation sin(sqrt(x**2 + y**2))
z = np.sin(np.sqrt(x**2 + y**2))

# --- Create the 3D surface plot ---
# Initialize a Plotly figure
fig = go.Figure(
    data=[go.Surface(z=z, x=x, y=y)]  # Add a 3D surface trace with z, x, and y data
)

# --- Customize layout ---
fig.update_layout(
    scene=dict(  # Configure scene settings
        xaxis_title='X Axis',  # Label the x-axis
        yaxis_title='Y Axis',  # Label the y-axis
        zaxis_title='Z Axis'  # Label the z-axis
    ),
    margin=dict(l=0, r=0, b=0, t=40),  # Adjust margins for visual clarity
    title='3D Surface Plot of sin(sqrt(x^2 + y^2))'  # Set the plot title
)

# --- Display the plot ---
fig.show()  # Render the interactive 3D surface plot
