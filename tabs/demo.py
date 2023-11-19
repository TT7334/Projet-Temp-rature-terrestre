import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def demo():
    st.write("Une fois qu'on à fait les prédicitions et qu'on les a concaténés dans un dataframe (sans oublié les années et en option la population). Il ne restera qu'à faire une mise en page ou l'utilisateur rentre l'année qu'il souhaite et s'affichera le chiffre prédit")
    st.write("Ensuite on compare nos prédictions avec le GIEC.")
