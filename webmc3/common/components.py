from dash import dependencies as dep
import dash_core_components as dcc
import dash_html_components as html

from ..utils import get_varname_options


def add_include_transformed_callback(app, title, trace):
    @app.callback(
        dep.Output('{}-selector'.format(title), 'options'),
        [dep.Input(
            '{}-selector-include-transformed'.format(title),
            'values'
        )]
    )
    def update_selector_transformed(values):
        return get_varname_options(
            trace,
            include_transformed=values
        )


def selector(title, trace, varname, include_transformed_chooser=True):
    children = [
        html.Label("Variable"),
        dcc.Dropdown(
            id='{}-selector'.format(title),
            options=get_varname_options(trace),
            value=varname
        )
    ]

    if include_transformed_chooser: 
        children.append(
            dcc.Checklist(
                id='{}-selector-include-transformed'.format(title),
                options=[{
                    'label': "Include transformed variables",
                    'value': 'include_transformed'
                }],
                values=[]
            )
        )

    return html.Div(children, style={'width': '20%'})
