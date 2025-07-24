# Import the Plotly Express library for creating interactive visualizations
import plotly.express as px

# Create a data frame
df = px.data.tips()

# View the contents of the data frame
print(df.head())

# Create a 3D line plot
fig = px.line_3d(df, x="total_bill", y="tip", z="size",color="day")

# Set the line color
fig.update_traces(line_color=["red", "green", "blue"])

# Display the plot
fig.show()