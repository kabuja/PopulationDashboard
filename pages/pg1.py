import pathlib 
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd 

dash.register_page(__name__, path='/')

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
   


df=pd.read_csv("https://raw.githubusercontent.com/kabuja/Dashboard/main/data/data%203.csv")
layout = html.Div(
    [
        
        dcc.Graph(id='line-fig',
                  figure=px.pie(df, values='total',names='continent',title='Total population per continent for the years, 2017, 2018, 2019, 2020, 2021, 2022, 2023'))
    ]
)

