from dash import html, dcc
import plotly.graph_objs as go

from utils import Header, make_dash_table_yc
import pandas as pd
import pathlib

def create_layout(app):
    df_yc = pd.read_csv("./data/treasury_yield_curve.csv")
    df_yc = df_yc.iloc[::-1]
    
    dropdown_dates = [{'label': i, 'value': i} for i in df_yc["NEW_DATE"]]
    dropdown_maturities = [ {'label': i, 'value': i} for i in df_yc.columns[2:-1]]

    df_yc_short = df_yc.iloc[:10]

    yc_plot_data = [
        go.Scatter(
            x = df_yc.columns[2:-1],
            y = df_yc.iloc[0][2:-1]
        )
    ]

    layout = html.Div(
        [
            html.Div([Header(app)]),
            html.Div(
                [   
                    html.Div(
                        [
                            html.Label('Select Dates:'),
                            dcc.Dropdown(
                                id = 'dropdown-yc',
                                options = dropdown_dates,
                                value=[df_yc.iloc[0][1]],
                                multi = True
                            ),
                            html.Br([])
                        ]
                    ),
                    html.Div(
                                [
                                    dcc.Graph(
                                        id="graph-yc",
                                        figure={
                                            "data": yc_plot_data,
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
                            html.Br([]),
                            html.Label('Select Maturities:'),
                            dcc.Dropdown(
                                id = 'dropdown-ts',
                                options = dropdown_maturities,
                                value=['BC_1MONTH'],
                                multi = True
                            ),
                            html.Br([])
                        ]
                    ),
                    html.Div(
                                [
                                    dcc.Graph(
                                        id="graph-ts",
                                        figure={
                                            "data": yc_plot_data,
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
                    html.Label('Daily Treasury Par Yield Curve Rates (Last 10 Days)'),
                    html.Table(make_dash_table_yc(df_yc_short)),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
    return layout
