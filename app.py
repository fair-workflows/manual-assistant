
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    html.H1(children='Manual Task Assistant')
    ])


if __name__ == '__main__':
    app.run_server(debug=True)