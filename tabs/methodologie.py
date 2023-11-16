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

def methodo():
    st.image("../assets/methodologie.jpg", use_column_width=True)
    # La première étape est de faire des prédictions sur le CO2
    st.write("Maintenant que nous avons constaté qu'il y avait bien un réchauffement des températures à l'échelle de la planète et que cette augmentation est fortement influencée par les emmissions de CO2 (principalement produites par l'industrialisation, essayons de prédire les changements de températures pour les années futures en prenant en compte les emissions de CO2 dans notre modèle")
    st.write("Voici donc la méthodologie que nous avons adoptée pour mener à bien notre projet:")
    texte = """
    - Nous nous sommes donc d'abord, nous nous sommes penchés sur les changements de températures:
        - Nettoyage complet de la base de données avec nottament la gestion des valeurs manquantes et l'encodage des variables
        - Test de différents modèles pour ne garder que le plus performant.
    - Une fois chose faite, nous nous sommes penchés sur les emissions de CO2:
        - Nettoyage complet de la base de données avec nottament la gestion des valeurs manquantes et l'encodage des variables
        - Test de différents modèles pour ne garder que le plus performant.
    """
    st.markdown(texte)
    st.markdown('<hr style="border: none; border-top: 2px solid #D3D3D3; width: 50%;">', unsafe_allow_html=True)
    st.subheader("I. Température :")
    st.write("**Nettoyage de la base de données:**")
    st.write("Ajouter le code avec la méthode des knn")
    st.write("Ajouter le code avec la fonction de suppression des valeurs manquantes")
    st.write("Ajouter le code de garder les années à partir de 1961")
    st.write("Afficher le tableur nettoyé")
    
    st.write("**Différents modèles utilisés:**")
    st.write("Expliquer qu'on veut le modèle le plus performant, nous en avons donc testé plusieurs.")
    st.write("Ajouter les codes de prophet, arbre de décision, régréssion linéaire et séries temporelles")
    st.write("Comparer la performance des modèles et choisir le plus performant")

    st.subheader("II. CO2 :")
    st.write("**Nettoyage de la base de données:**")
    st.write("Ajouter le code avec la méthode des knn")
    st.write("Ajouter le code avec la fonction de suppression des valeurs manquantes")
    st.write("Ajouter le code de garder les années à partir de 1961")
    st.write("Afficher le tableur nettoyé")
    
    st.write("**Différents modèles utilisés:**")
    st.write("Expliquer qu'on veut le modèle le plus performant, nous en avons donc testé plusieurs.")
    st.write("Ajouter les codes de prophet, arbre de décision, régréssion linéaire")
    st.write("Comparer la performance des modèles et choisir le plus performant")

    st.write("Conclure en faisant une transition sur la démonstration")

