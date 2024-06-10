import pandas as pd
import plotly.express as px
from shiny import App, ui, render
#from shiny.express import input, ui
from shinywidgets import render_widget, output_widget
import nest_asyncio
nest_asyncio.apply()

# import dataFrame
#df = pd.read_json('/Users/ellandalla/Desktop/Portfolio/Unsupervised/data.json')
df = pd.read_csv('/Users/ellandalla/Desktop/Portfolio/Unsupervised/data.csv')
missing = [column for column in df.columns if df[column].isnull().any()]
color_mapping = {'0': 'green', '1': 'orange'}

# Create plotly map
def create_map_plot():
    fig = px.scatter_mapbox(
        df,
        lat='latitude',
        lon='longitude',
        size='square_feet',
        color='prediction_label',
        color_discrete_map=color_mapping,
        hover_name='cityname',
        hover_data={
            'state': True,
            'price': True,
            'sports_count': True,
            'outdoor_count': True,
            'luxury_count': True,
            'convenience_count': True
        },
        zoom=4,
        height=1000,
    )
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(title_text="US Rental Market")
    fig.update_layout(legend=dict(
            title="Prediction Label",
            x=0,
            y=1,
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=12,
                color="black"
            ),
            bgcolor="rgba(255,)",
            bordercolor="rgba(0, 0, 0, 0.1)",
            borderwidth=1))
    
    return fig

#fig.show(create_map_plot())
# Save the Plotly figure as an HTML file
fig = create_map_plot()
fig.write_html("map_plot.html")

# Read the HTML content
with open("map_plot.html", "r") as f:
    plot_html = f.read()
    

# Define Shiny UI
app_ui = ui.page_fluid(
    ui.h2(" US Rental Market Interactive Map"),
    ui.HTML(plot_html) 
)

# Define Shiny server logic
def server(input, output, session):
    pass


# Create the Shiny app
rent_app = App(app_ui, server)

if __name__ == "__main__":
    rent_app.run()
    
