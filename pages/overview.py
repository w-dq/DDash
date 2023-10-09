from dash import html, dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State


from utils import Header

import pandas as pd
import pathlib
import datetime


def create_layout(app):
    current_year = int(datetime.date.today().year)
    yc_years = [{'label': str(i), 'value': str(i)} for i in range(current_year,2000,-1)]
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Overview"),
                                    html.Br([]),
                                    html.P(
                                        "This is a dashboard for data monitoring, it currently has only yield curve and Fed Funds target data from FRED and treasury.gov",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    html.Div(
                        [   
                            html.Div([
                                html.H5("Yield Curve"),
                                html.P(
                                    "To use the Yield Curve page:\
                                    - For the first time or to update data, click the 'Update Yield Curve Data' button and wait for it to turn green.\
                                    - This would take about 5 seconds.",
                                    style={ 'margin-right': '10px'}
                                ),
                            ],style={'display': 'inline-block', 'width': '50%'}),
                            html.Div([
                                dcc.Dropdown(
                                    id='dropdown-yc-project',
                                    options=yc_years,
                                    value=[str(current_year)],
                                    multi=True,
                                    style={'display': 'inline-block', 'width':'100%'}
                                ),
                                html.Button("Update Yield Curve Data", 
                                    id="update-yc",
                                    style={'display': 'inline-block'},
                                ),
                                dcc.Store(id="yc_n_clicks-store", data=0)
                            ],style={'display': 'inline-block', 'width':'50%'})
                        ], className = "project-container")
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
