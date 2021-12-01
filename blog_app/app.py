from dash import (
    Dash,
    Input,
    Output,
    State,
    html,
    dcc,
    callback,
    callback_context,
    exceptions,
)
import dash_bootstrap_components as dbc

from flask import Flask, redirect

from pages import (
    new_page
)


server = Flask(__name__)  # define flask app.server
server.config["SECRET_KEY"] = "TOM"

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    routes_pathname_prefix="/blog-beast/",
    server=server,
)
app.title = "Tom's Blog"
app.config.suppress_callback_exceptions = True
app.layout = html.Div([dcc.Location(id="url", refresh=False), html.Div(id="page-content")])


@server.route("/")
def home():
    """Landing page."""
    return redirect("blog-beast/new")

 # Callback for navigating between pages
@callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/blog-beast/new":
        return new_page


if __name__ == "__main__":
    app.run_server()
