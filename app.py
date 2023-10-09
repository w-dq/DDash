import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

from pages import (
    overview,
    yield_curve,
)
import pandas as pd
from proccess import update_yield_curve_data

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    suppress_callback_exceptions=True
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
    Input('dropdown-yc-project', 'value'),
    Input('update-yc', 'n_clicks'),
    prevent_initial_call=True
)
def yield_curve_update(years, n_clicks):
    print("Updating Yield Curve")
    button_style = dict()
    if n_clicks is None:
        print("No Clicks")
        return  button_style
    res = update_yield_curve_data(years)
    if res:
        button_style['background-color'] = '#009b9d'
        button_style['pointer-events'] = 'none'
        print("Finished Updating Yield Curve")
    else:
        button_style['background-color'] = '#ed1c24'
        button_style['pointer-events'] = 'none'
        print("Failed Updating Yield Curve")
    return button_style

@app.callback(
    Output('graph-yc', 'figure'),
    Input('dropdown-yc', 'value')
)
def rerender_yc_graph(selected_date):
    df_yc = pd.read_csv("./data/treasury_yield_curve.csv")

    filtered_df = df_yc[df_yc['NEW_DATE'].isin(selected_date)]
    x_labels = df_yc.columns[2:-1]

    yc_plot_data = []
    for index, row in filtered_df.iterrows():
        g = go.Scatter(
            x = x_labels,
            y = df_yc.iloc[index][2:-1],
            name=row["NEW_DATE"]
        )
        yc_plot_data.append(g)
    return {"data": yc_plot_data}

@app.callback(
    Output('graph-ts', 'figure'),
    Input('dropdown-ts', 'value')
)
def rerender_ts_graph(selected_cols):
    df_yc = pd.read_csv("./data/treasury_yield_curve.csv")
    df_yc['NEW_DATE'] = pd.to_datetime(df_yc['NEW_DATE'])

    ts_plot_data = []
    for col in selected_cols:
        g = go.Scatter(
            x = df_yc['NEW_DATE'],
            y = df_yc[col],
            name = col
        )
        ts_plot_data.append(g)
    return {"data": ts_plot_data}

@app.callback(
    Output('graph-sp', 'figure'),
    Input('dropdown-sp-1', 'value'),
    Input('dropdown-sp-2', 'value')
)
def rerender_sp_graph(col_1,col_2):
    df_yc = pd.read_csv("./data/treasury_yield_curve.csv")
    df_yc['NEW_DATE'] = pd.to_datetime(df_yc['NEW_DATE'])
    df_yc['SPREAD'] = df_yc[col_2] - df_yc[col_1]
    sp_plot_data = [
        go.Scatter(
            x = df_yc['NEW_DATE'],
            y = df_yc['SPREAD'],
            name = 'Spread'
        )
    ]
    return {"data": sp_plot_data}

if __name__ == "__main__":
    app.run_server(debug=True, port=8070)