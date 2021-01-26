import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from manualassistant import manual_step
from fairworkflows import FairStep

HOST = '0.0.0.0'

EXAMPLE_STEP_URI = 'http://test-server.nanopubs.lod.labs.vu.nl/RALgfqDcbpRvQ9HWXnPPtTzqeNvFBdBc7p4ZcbxqEg0fs'


def create_outputs(step: FairStep):
    output_checks = [{'label': str(o), 'value': str(o)} for o in step.outputs]
    return dcc.Checklist(options=output_checks)


def create_layout(step):
    return dbc.Container(children=[
        dcc.Location(id='url', refresh=False),
        dbc.Row([
            html.H1(children='Manual Task Assistant')
        ]),
        dbc.Row(children=[
            html.Blockquote(step.description)]),
        dbc.Row(
            children=create_outputs(step)),
        dbc.Row(children=[
            html.Button('Confirm')
        ])
    ])


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            'external_stylesheets=[dbc.themes.SPACELAB]',
        ]
    )

    step = manual_step.get_manual_step(EXAMPLE_STEP_URI)

    dash_app.layout = create_layout(step)

    return dash_app.server
