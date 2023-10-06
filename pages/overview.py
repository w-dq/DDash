from dash import html, dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

from utils import Header

import pandas as pd
import pathlib


def create_layout(app):
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
                                    html.P(
                                        "To use the Yield Curve page:",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.P(
                                        "- For the first time or to update data, click the 'Update Yield Curve Data' button and wait for it to turn green.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.P(
                                        "- This would take about 5 seconds.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                html.Button("Update Yield Curve Data", id="update-yc"),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
