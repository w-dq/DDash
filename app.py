import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from pages import (
    overview,
    yield_curve,
)

from proccess import update_yield_curve_data

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    # suppress_callback_exceptions=True
)
app.title = "Daqian Dashboard"

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/daqian-dashboard/yieldcurve":
        return yield_curve.create_layout(app)
    else:
        return overview.create_layout(app)

@app.callback(
    Output('update-yc', 'style'),
    Input('update-yc', 'n_clicks'),
    prevent_initial_call=True
)
def yield_curve_update(n_clicks):
    print("Updating Yield Curve")
    button_style = dict()
    if n_clicks is None:
        print("No Clicks")
        return  button_style
    res = update_yield_curve_data(["2023"])
    print("res")
    button_style['background-color'] = '#009b9d'
    button_style['pointer-events'] = 'none'
    print("Finished Updating Yield Curve")
    return button_style

if __name__ == "__main__":
    app.run_server(debug=True, port=8070)