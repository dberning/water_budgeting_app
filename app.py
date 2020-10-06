import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

catchment_div_containers = []

app.layout = html.Div([
    html.H1('Water Usage Estimator'),
    html.P("This is a small web-application for estimating how much water a particular property produces annually"),
    html.Div(catchment_div_containers, id='catchment-section'),
    html.Button("Add another catchment", id='add-catchment-btn')
])


@app.callback(
    Output(component_id='catchment-section', component_property='children'),
    [Input(component_id='add-catchment-btn', component_property='n_clicks')])
def add_new_catchment_section(clicks):
    if clicks:
        for click in range(clicks-len(catchment_div_containers)):
            catchment_div_containers.append(
                html.Div(id='catchment-'+str(len(catchment_div_containers)), children=[
                    html.H3("This is a new catchment"),
                    html.P("This will contain information about a catchment"),
                    html.Button("Remove", id='remove-catchment-'+str(len(catchment_div_containers)))
                ])
            )

    return catchment_div_containers

@app.callback(
    Output(component_id='catchment-section', component_property='children'),
    [Input(component_id='add-catchment-btn', component_property='n_clicks')])
def add_new_catchment_section(clicks):
    pass

if __name__ == "__main__":
    app.run_server(port=8000, debug=True)
