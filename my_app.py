import dash
from dash import html, dcc
import pathlib 


my_app = dash.Dash(__name__, use_pages=True)

server = my_app.server
my_app.layout = html.Div(
    [
        # main app framework
        html.Div("WorldWide Population Distribution", style={'fontSize':50, 'textAlign':'center'}),
        html.Div([
            dcc.Link(page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),

        # content of each page
        dash.page_container
    ]
)


if __name__ == "__main__":
    my_app.run(debug=False,port=5069)
