import base64
import os

from dash import html
import dash_bootstrap_components as dbc

def create_img(img_path: str, height: int, style: dict = {}):
    encoded_image = base64.b64encode(open(os.path.join(os.getcwd(), img_path), "rb").read())
    return html.Img(
        src="data:image/png;base64,{}".format(encoded_image.decode()),
        height=height,
        style=style,
    )

logo = html.Div(
    create_img("data/tomato.jpeg", 100),
    style={"left": "10%", "position": "fixed", "zIndex": "4"},
)
title = html.Div(
    create_img("data/title.png", 100),
    style={"left": "38.8%", "position": "fixed", "zIndex": "4"},
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(
                    html.H6(dbc.NavLink("History of War and Conflict", href="/blog-beast/history-of-war-and-conflict", style={"color": "white"})),
                    header=True,
                ),
                dbc.DropdownMenuItem(
                    html.H6(dbc.NavLink("Ancient Peoples", href="/blog-beast/ancient-peoples", style={"color": "white"})),
                    header=True,
                ),
            ],
            caret=False,
            color="white",
            label=" - ",
            direction="down",
            style={
                "right": "10%",
                "top": "3%",
                "position": "fixed",
                "zIndex": "5",
                "height": 50,
            },
            in_navbar=True,
        ),
        create_img(
            "data/tomato.jpeg",
            100,
            {"right": "9.3%", "top": "0%", "position": "fixed", "zIndex": "3"},
        ),
    ],
    color="black",
    style={"height": 60},
    dark=True,
)

home_page = html.Div(
    [
        logo,
        title,
        navbar,
    ]
)

war_page = html.Div(
    [
        logo,
        title,
        navbar,
        html.Br(),
        html.Br(),
        html.H5('History of War and Conflict')
    ]
)

ancients_page = html.Div(
    [
        logo,
        title,
        navbar,
        html.Br(),
        html.Br(),
        html.H5('Ancient Peoples')
    ]
)
