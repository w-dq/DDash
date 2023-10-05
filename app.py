import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from pages import (
    overview,
    yield_curve,
)

from proccess import update_yield_curve_data

def update_background():
    print("updating data in background")
    update_yield_curve_data(["2023"])
    print("data update complete")


    



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

if __name__ == "__main__":
    app.run_server(debug=True, port=8070)
    

