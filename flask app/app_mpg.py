from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import mpgdata as ds
import plotly.express as px

# Initialize app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# Build components
header = html.H2("MPG Analysis Dashboard", className="text-center alert alert-info")
bar1 = px.bar(ds.get_pivot_data(), x = "model year", y = "car name", color = "origin", barmode="group", width=800, title="Number of cars by model year and country",
              labels={"car name" : ""})
hist1 = px.histogram(ds.df, x = "origin", y = "mpg", text_auto=True, color = "origin", width=500, histfunc="avg")
scatter1 = px.scatter(ds.df, x = "horsepower", y = "mpg", width = 800, facet_col = "origin", trendline="ols")
pairplot1 = px.scatter_matrix(ds.df, dimensions=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration'], height=600)

# App Layout
app.layout = html.Div([ header, html.Hr(),
                       dcc.Graph(figure=bar1, id="bar1"), html.Br(),
                       dcc.RadioItems(options = ["ALL", "USA", "Germany", "Japan"], value = "ALL", id = "radio_filter", 
                                      className="d-flex flex-wrap align-content-center gap-1 justify-content-center"),
                       dbc.Row(
                           [
                               dbc.Col(dcc.Graph(figure=hist1, id="hist1")),
                               dbc.Col(dcc.Graph(figure=scatter1, id="scatter1")),
                           ], 
                       ),
                       dcc.Graph(figure=pairplot1, id="pairplot1")
])


@callback(
        Output(component_id = "hist1", component_property="figure"),
        Output(component_id = "scatter1", component_property="figure"),
        Output(component_id = "pairplot1", component_property="figure"),
        Input(component_id= "radio_filter", component_property="value")
)
def radio_action(input_value):    
    if input_value == "ALL" :
        data = ds.df
    else :
        data = ds.df[ds.df.origin == input_value]

    hist1 = px.histogram(data, x = "origin", y = "mpg", text_auto=True, color = "origin", width=500, histfunc="avg")
    scatter1 = px.scatter(data, x = "horsepower", y = "mpg", width = 800, facet_col = "origin", trendline="ols")
    pairplot1 = px.scatter_matrix(data, dimensions=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration'], height=600)

    return hist1, scatter1,pairplot1


# Run the app
if __name__ == "__main__" :
    app.run_server()
