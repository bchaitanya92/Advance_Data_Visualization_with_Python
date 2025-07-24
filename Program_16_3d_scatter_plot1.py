# Import the Plotly Express library for creating interactive visualizations
import plotly.express as px

# Define data for the 3D scatter plot
# - size: A list of numerical values representing the size of the markers
size = [10, 20, 30, 40, 50]

# - x, y, z: Coordinate values for each point in the 3D space
x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 7, 8]
z = [7, 8, 9, 10, 11]

# Create a 3D scatter plot using Plotly Express
fig = px.scatter_3d(
    x=x,  # Assign x-axis data
    y=y,  # Assign y-axis data
    z=z,  # Assign z-axis data
    size=size,  # Map marker sizes to the 'size' list
)

# Display the interactive 3D scatter plot
fig.show()
