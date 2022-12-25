import pathlib
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd 

dash.register_page(__name__)

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()


df=pd.read_csv("https://raw.githubusercontent.com/kabuja/Dashboard/main/data/data4.csv")

layout = html.Div(
    [
        dcc.Dropdown([x for x in df.country.unique()], id='cont-choice', style={'width':'50%'}),
        dcc.Graph(id='line-fig',
                  figure=px.bar(df, x='year', y='population',color='year',title='Population Distribution Per Country Per Year'))
    ]
)
