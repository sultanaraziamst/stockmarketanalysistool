import dash 
import dash_bootstrap_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output 
import plotly.graph_objects as graph_objects
import pandas as pd 
import yfinance as yf 


app = dash.Dash(__name__)


def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, start = '2022-01-01', end = '2024-06-01')
    stock_data.reset_index(inplace=True)
    return stock_data
