#Tyler Pickard
from jupyter_plotly_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
import dash
import dash_leaflet as dl
import plotly.express as px
import dash_table
from dash.dependencies import Input, Output
from pymongo import MongoClient
import urllib.parse
from bson.json_util import dumps
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#ToDo: Import for their CRUD Module
from modulep4.py import AnimalShelter

#update with my mongodb login
username = "aacuser"
password = "accpass"
shelter = AnimalShelter(username, password)

#allows for read funciton
df = pd.DataFram.from_records(shelter.read({}))
#this is a juypter dash application
app = JupyterDash('Animal Shelter Dashboard')

#the application interfaces are declared here
#this application has two input boxes, a submit box, a horizontal line and div for Output

app.layout = html.Div(
    [
        html.Div(id='hidden-div', style={}'display': 'none'}),
        html.Center(html.B(html.H1("Tyler Pickard's Animal Shelter Dashboard"))),
        html.Hr(),
        dash_table.DataTable(
        id='datatable-id',
        columns=[
            {"name": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        data-df.to_dict('records'),

        #FIXME correct the CRUD method
        create,
        read,
        update,
        delete
        )

    ]
) #end of html Div

#callback for the table
@app.callback(
    Output('datatable-id', 'style_data_conditional'),
    [Input('datatable-id', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
    'if': {'column_id': i},
    'background_color': '#D2F3FF'    #highlights the selected columns
    } for i in selected_columns]
#this is area to define application responses or callback routines
#this one callback will take the entered text and if the submit button is click then call
#the mongo database with the fine_one query and returen the result to the output Div
@app.callback(
Output("query-out", "children"),
[Input("input_user".format("text"), "value"),
Input("input_passwd".format("password"), "value"),
Input("submit-val", 'n_clicks')],
[dash.dependencies.State('input_passwd', 'value')]
)

def cb_render(userValue, passValue, n_clicks, buttonValue):
    if n_clicks > 0:
        #data manipulation
        #use crud module to access mongodb
        username = urllib.parse.quote_plus(aacuser)
        password = urllib.parse.quote_plus(aacpass)

        #todo: eneter curb objectid

#Add Geolocation Chart
def update_map(viewData):
    dff = pd.DataFrame.from_dict(viewData)
    #Austin Tx is at [30.75, -97.48]
    return[
        d1.Map(style = {'width': '1000px', 'height': '500px'}, center[20.75, -97.48], zoom=10, children=[]
        d1.TileLayer(id="base-layer-id"),
        d1.Marker(position=[30.75, -97.48], children=[
        d1.Tooltip(diff.iloc[0, 4]),
        d1.Popup([
            html.H1("Animal Name"),
            html.P(dff.iloc[1, 9])
        ])
        ])
        ])
    ]

#example query
self.database.animals.find("animal_type": "Dog", "name": "Lucy")

app #end of app
