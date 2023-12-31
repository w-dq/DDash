from dash import html, dcc

def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])

def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.A(
                        html.Img(
                            src=app.get_asset_url("dashboard_logo.png"),
                            className="logo",
                        )
                    ),
                    html.A(
                        html.Button(
                            "Contact",
                            id="learn-more-button",
                            style={"margin-left": "-10px"},
                        ),
                        href="mailto:daqian.wu@proton.me?subject=DaqianDashboard",
                    ),
                    html.A(
                        html.Button("Source Code", 
                            id="learn-more-button"
                    ),
                        href="https://github.com/w-dq/DDash"
                    ),
                ],
                className="row",
            )
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/daqian-dashboard/overview",
                className="tab first",
            ),
            dcc.Link(
                "Yield Curve",
                href="/daqian-dashboard/yieldcurve",
                className="tab",
            ),
            dcc.Link(
                "Option Pricing",
                href="/daqian-dashboard/vanillaoption",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu

def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(0,len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

def make_dash_table_yc(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    header = [html.Th(col) for col in df.columns[1:-1]]
    header_row = html.Tr(header)

    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(1,len(row)-1):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    table = [header_row] + table
    return table

def remove_namespace(tag):
    return tag.split('}')[1] if '}' in tag else tag