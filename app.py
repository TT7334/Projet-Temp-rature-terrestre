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

#PARTIE SIDEBAR
color_code="#4628DD"
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: ##D3D3D3;
    }
</style>
""", unsafe_allow_html=True)

#A récupérer le logo de datascientest
st.sidebar.image("./assets/logo_datascientest.png")

# Case à cocher pour la navigation entre les pages
from introduction import introduction_projet
from preprocessing import prepro
from datavisualisation import dataviz
from methodologie import methodo
from demo import demo
PAGES = {
    "Introduction du projet": introduction_projet,
    "Pre-processing":prepro,
    "Datavisualisation": dataviz,
    "Méthodologie de la modélisation": methodo,
    "Démonstration des prédictions": demo,
}
st.sidebar.markdown("## Sommaire:")
selection = st.sidebar.radio("Sélectionnez une page :", list(PAGES.keys()))
page = PAGES[selection]
page()

# Liste des contributeurs
st.sidebar.markdown("## Contributeurs:")
st.sidebar.markdown("Yasmine Kouyaté")
st.sidebar.markdown("Jean-Michel Deblaise")
st.sidebar.markdown("Youcef Arim")
st.sidebar.markdown("Théo Delafontaine")

# Promotion
st.sidebar.markdown("## Promotion:")
st.sidebar.write("avr23_continu_da")
