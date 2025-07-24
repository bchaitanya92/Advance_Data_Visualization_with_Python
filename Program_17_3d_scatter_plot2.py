# Import the Plotly Express library for creating interactive visualizations
import plotly.express as px

# Create a data frame
df = px.data.tips()
print(df)

# View the contents of the data frame
print(df.head())

# Create a 3D scatter plot
fig = px.scatter_3d( df, x="total_bill", y="tip", z="size", color="day")

# Display the plot
fig.show()