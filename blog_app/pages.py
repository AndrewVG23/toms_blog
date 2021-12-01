import base64
import os
import pandas as pd

from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

def create_img(img_path: str, height: int, style: dict = {}):
    encoded_image = base64.b64encode(open(img_path, "rb").read())
    return html.Img(
        src="data:image/png;base64,{}".format(encoded_image.decode()),
        height=height,
        style=style,
    )

logo = html.Div(
    create_img("blog_app/data/tomato.jpeg", 100),
    style={"left": "7%", "position": "fixed", "zIndex": "4"},
)
title = html.Div(
    create_img("blog_app/data/title.png", 100),
    style={"left": "38.8%", "position": "fixed", "zIndex": "4"},
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(
                    html.H6(dbc.NavLink("New", href="/concept-maps/new", style={"color": "white"})),
                    header=True,
                ),
                dbc.DropdownMenuItem(
                    html.H6(
                        dbc.NavLink(
                            "Update",
                            href="/concept-maps/update",
                            style={"color": "white"},
                        )
                    ),
                    header=True,
                ),
            ],
            caret=False,
            color="white",
            label=" - ",
            direction="down",
            style={
                "right": "7.7%",
                "top": "1.29%",
                "position": "fixed",
                "zIndex": "5",
                "height": 50,
            },
            in_navbar=True,
        ),
        create_img(
            "blog_app/data/tomato.jpeg",
            100,
            {"right": "7%", "top": "0%", "position": "fixed", "zIndex": "3"},
        ),
    ],
    color="black",
    style={"height": 60},
    dark=True,
)



new_page = html.Div(
    [
        logo,
        title,
        navbar,
    ]
)
