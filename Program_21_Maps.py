import plotly.express as px
import pandas as pd

# Import data from the specified GitHub URL and create a Pandas DataFrame
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

fig = px.choropleth(data,                               # Create a basic choropleth map using Plotly Express
                    locations='iso_alpha',              # The 'iso_alpha' column specifies the country codes for locations,
                    color='gdpPercap',                  # the 'gdpPercap' column determines the color intensity based on GDP per capita,
                    hover_name='country',               # and 'hover_name' provides country names for hover information.
                    projection='natural earth',         # The map is projected in the natural earth view.
                    title='GDP per Capita by Country'   # The title of the map is set to 'GDP per Capita by Country'.
                    )

# Display the choropleth map
fig.show()
