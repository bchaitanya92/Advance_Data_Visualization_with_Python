# - plotly.graph_objects: Provides tools for creating and customizing interactive visualizations
import plotly.graph_objects as go
# - numpy: Offers powerful array and numerical computation capabilities
import numpy as np

# Create a 50x50 array of random numbers
z = np.random.randn(50, 50)

# Create a Surface trace
surface = go.Surface(x=np.arange(50), y=np.arange(50), z=z)

# Create a Figure object
fig = go.Figure(data=[surface])

# Show the plot
fig.show()
