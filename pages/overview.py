from dash import html, dcc
import plotly.graph_objs as go

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
                                    html.H5("Product Summary"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    As the industry’s first index fund for individual investors, \
                                    the Calibre Index Fund is a low-cost way to gain diversified exposure \
                                    to the U.S. equity market. The fund offers exposure to 500 of the \
                                    largest U.S. companies, which span many different industries and \
                                    account for about three-fourths of the U.S. stock market’s value. \
                                    The key risk for the fund is the volatility that comes with its full \
                                    exposure to the stock market. Because the Calibre Index Fund is broadly \
                                    diversified within the large-capitalization market, it may be \
                                    considered a core equity holding in a portfolio.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
