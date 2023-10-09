from dash import html, dcc
import plotly.graph_objs as go

from utils import Header, make_dash_table_yc
import pandas as pd
import pathlib

def create_layout(app):
    try:
        df_yc = pd.read_csv("./data/treasury_yield_curve.csv")
        df_fedtaru = pd.read_csv("./data/DFEDTARU.csv")
        df_fedtarl = pd.read_csv("./data/DFEDTARL.csv")
    except:
        layout =  html.Div([
                                html.Div([Header(app)]),
                                html.Div([
                                    html.H2("Make sure treasury_yield_curve.csv, DFEDTARU.csv and DFEDTARL.csv are in place, go to overview to see more instruction.")
                                ], style = {'color':"#ed1c24"}),
                            ])
        return layout

    target_upper = df_fedtaru.iloc[-1]["DFEDTARU"]
    target_lower = df_fedtarl.iloc[-1]["DFEDTARL"]
    
    dropdown_dates = [{'label': i, 'value': i} for i in df_yc["NEW_DATE"]]
    dropdown_maturities = [ {'label': i, 'value': i} for i in df_yc.columns[2:-1]]

    df_yc_short = df_yc.iloc[:10]

    layout = html.Div(
        [
            html.Div([Header(app)]),
            html.Div(
                [   
                    html.Div(
                        [
                            html.Label(f"Federal Funds Target Range: \
                                        Overnight Reverse Repurchase rate (ONRRP) {target_lower}, \
                                        Interest on Excess Reserves (IOER) {target_upper}")
                        ], style = {'fontSize':18}
                    ), 
                    html.Div(
                        [
                            html.H5("Yield Curve")
                        ], style = {'color': '#009b9d'}
                    ),
                    html.Div(
                        [
                            html.Label('Select Dates:'),
                            dcc.Dropdown(
                                id = 'dropdown-yc',
                                options = dropdown_dates,
                                value=[df_yc.iloc[0][1]],
                                multi = True
                            )
                        ]
                    ),
                    html.Div(
                                [
                                    dcc.Graph(
                                        id="graph-yc",
                                        figure={
                                            "layout": go.Layout(
                                                title="Yield Curve",
                                                autosize=True,
                                                height=400,
                                                xaxis={
                                                    "autorange": True,
                                                    "showgrid": True,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "showgrid": True,
                                                }
                                            )
                                        }
                                    )
                                ]
                            ),
                    html.Div(
                        [
                            html.H5("Term Structure")
                        ], style = {'color': '#009b9d'}
                    ),
                    html.Div(
                        [
                            html.Label('Select Maturities:'),
                            dcc.Dropdown(
                                id = 'dropdown-ts',
                                options = dropdown_maturities,
                                value=['BC_1MONTH'],
                                multi = True
                            )
                        ]
                    ),
                    html.Div(
                                [
                                    dcc.Graph(
                                        id="graph-ts",
                                        figure={
                                            "layout": go.Layout(
                                                title="Term Structure",
                                                autosize=True,
                                                height=400,
                                                xaxis={
                                                    "autorange": True,
                                                    "showgrid": True,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "showgrid": True,
                                                }
                                            )
                                        }
                                    )
                                ]
                            ),
                    html.Br([]),
                    html.Div(
                        [
                            html.H5("Spread")
                        ], style = {'color': '#009b9d'}
                    ),
                    html.Label('Select Spread Maturities:'),
                    html.Div(
                                [
                                    dcc.Dropdown(
                                        id='dropdown-sp-1',
                                        options= dropdown_maturities,
                                        value='BC_1YEAR',
                                        placeholder = 'BC_1YEAR'
                                    )
                                ], style={'width': '48%', 'display': 'inline-block'}
                            ),
                    html.Div(
                                [
                                    dcc.Dropdown(
                                        id='dropdown-sp-2',
                                        options = dropdown_maturities,
                                        value='BC_10YEAR',
                                        placeholder = 'BC_10YEAR'
                                )
                                ], style={'width': '48%', 'display': 'inline-block'}
                            ),
                    html.Div(
                                [
                                    dcc.Graph(
                                        id="graph-sp",
                                        figure={
                                            "layout": go.Layout(
                                                title="Spread",
                                                autosize=True,
                                                height=400,
                                                xaxis={
                                                    "autorange": True,
                                                    "showgrid": True,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "showgrid": True,
                                                }
                                            )
                                        }
                                    )
                                ]
                            ),
                    html.Br([]),
                    html.Label('Daily Treasury Par Yield Curve Rates (Last 10 Days)'),
                    html.Table(make_dash_table_yc(df_yc_short)),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
    return layout
