import dash 
import dash_bootstrap_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output 
import plotly.graph_objects as graph_objects
import pandas as pd 
import yfinance as yf 


app = dash.Dash(__name__)
