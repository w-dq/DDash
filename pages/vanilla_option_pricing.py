from dash import html, dcc
import plotly.graph_objs as go

from utils import Header, make_dash_table_yc
import pandas as pd
from datetime import datetime

def create_layout(app):
    layout = html.Div(
        [
            html.Div([Header(app)]),
            html.Div([
                # html.H5("Option Pricing", style={"color":"#009b9d"}),
               html.Div([
                    html.Div([], className="two columns"),
                    html.Div([
                        html.Label("Underlying*"),
                        dcc.Input(id='op-underlying', type='text', placeholder='Underlying')
                    ], className="two columns", style={'margin-right':'30px'}),
                    html.Div([
                        html.Label("Strike*"),
                        dcc.Input(id='op-strike', type='text', placeholder='Strike')
                    ], className="two columns", style={'margin-right':'30px'}),
                    html.Div([
                        html.Label("Time to Maturity*"),
                        dcc.Input(id='op-direct-maturity', type='text', placeholder='Time to Maturity')
                    ], className="two columns", style={'margin-right':'30px'}),
                    html.Div([
                        html.Label("Volatility*"),
                        dcc.Input(id='op-volatility', type='text', placeholder='Volatility')
                    ], className="two columns", style={'margin-right':'30px'}),
                    html.Div([
                        html.Label("Risk-Free Rate*"),
                        dcc.Input(id='op-risk-free-rate', type='text', placeholder='Risk-Free Rate')
                    ], className="two columns"),
                ], className="row"),

                html.Div([
                    html.Div([], className="two columns", style={'margin-right':'30px'}),
                    html.Div([
                        html.Label("Number of Steps"),
                        dcc.Input(id='op-steps', type='text', placeholder='N')
                    ], className="two columns", style={'margin-right':'30px'}),
                    html.Div([
                        html.Label("Knock In"),
                        dcc.Input(id='op-knock-in', type='text', placeholder='Knock In Level')
                    ], className="two columns", style={'margin-right':'30px'}),
                    html.Div([
                        html.Label("Knock Out"),
                        dcc.Input(id='op-knock-out', type='text', placeholder='Knock Out Level')
                    ], className="two columns", style={'margin-right':'30px'}),
                    html.Div([
                        html.Label("Option Style*"),
                        dcc.Dropdown(
                            id = 'op-option-style',
                            options = [
                                {'label': 'American', 'value': 'A'},
                                {'label': 'European', 'value': 'E'}
                            ],
                            value='E',
                            multi = False
                        ),
                    ],className="two columns", style={'margin-right':'30px'}),
                    html.Div([
                        html.Label("Option Type*"),
                        dcc.Dropdown(
                            id = 'op-option-type',
                            options = [
                                {'label': 'Call Option', 'value': 'call'},
                                {'label': 'Put Option', 'value': 'put'}
                            ],
                            value='call',
                            multi = False)
                    ],className="two columns")
                ], className="row"),
                html.Div([
                    html.Div([], className="four columns"),
                    html.Div([
                        html.Button("Calculate BSM Option Price", id='calculate-bsm')
                        ],className="four columns",style={'margin-right':'10px'}),
                    dcc.Store(id="bsm-clicks-store", data=0),
                    html.Div([
                        html.Button("Binomial Tree Option Price", id='calculate-bt')
                        ],className="four columns",style={'margin-right':'10px'}),
                    dcc.Store(id="bt-clicks-store", data=0)
                ],className="row"),
                html.Br([]),
                html.Div([
                    html.H6("Price: ",style={'display':'inline-block','margin-right':"30px"}),
                    html.Div(id='output-result-bsm',children="Empty",style={'display':'inline-block'})
                ]),
                html.Div([
                    html.H6("Price:",style={'display':'inline-block','margin-right':"30px"}),
                    html.Div(id='output-result-bt',children="Empty",style={'display':'inline-block'})
                ])
            ],className="sub_page"),
        ],
        className="page")
    return layout