import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from bokeh.plotting import figure, show, output_notebook, output_file
from bokeh.models import HoverTool, ColumnDataSource, CategoricalColorMapper, Legend, LegendItem, Range1d, FixedTicker, Label, LabelSet
from bokeh.layouts import gridplot, column, row
from bokeh.palettes import Category20
from bokeh.models.annotations import Title
from bokeh.models.tickers import FixedTicker
from bokeh.models import GeoJSONDataSource
from scipy.stats import gaussian_kde
from scipy.stats import pearsonr
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as py
def demo():
    st.write("rajouter les éléments")