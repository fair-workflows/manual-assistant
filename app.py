import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

HOST = '0.0.0.0'
PORT = 8080

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = html.Div(children=[
    html.H1(children='Manual Task Assistant'),
    html.Div(children=[
        html.Blockquote('Task description etc'),
        html.Div(children=[
            'Output 1',
            dcc.Input('Output 1')]),
        html.Button('Confirm')
    ]
    )
]
)

if __name__ == '__main__':
    app.run_server(debug=True, host=HOST, port=PORT)
