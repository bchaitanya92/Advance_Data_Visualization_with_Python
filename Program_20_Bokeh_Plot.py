from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend, LegendItem, Span

# Specify the output file for the interactive plot
output_file("line_graph_with_annotations.html")

# Sample data for the lines
x = [1, 2, 3, 4, 5]
y1 = [2, 5, 7, 2, 8]
y2 = [1, 4, 5, 3, 6]

# Create the Bokeh figure with title and labels
p = figure(
    title="Line Graph with Annotations and Legends",
    x_axis_label="X-axis",
    y_axis_label="Y-axis"
)

# Add the lines to the plot
line1 = p.line(x, y1, line_width=2, color="blue", legend_label="Line 1")
line2 = p.line(x, y2, line_width=2, color="red", legend_label="Line 2")

# Add a vertical annotation (line) at x = 3
annotation = Span(location=3, dimension='width', line_color='black', line_width=8)
p.add_layout(annotation)

# Create a legend and add it to the plot
legend = Legend(items=[
    LegendItem(label="Line 1", renderers=[line1]),
    LegendItem(label="Line 2", renderers=[line2]),
])
p.add_layout(legend)

# Display the interactive plot
show(p)
