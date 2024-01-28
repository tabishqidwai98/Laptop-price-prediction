import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import plotly.express as px
import streamlit as st

df = pd.read_csv("C:/Users/tabis/Desktop/Laptop price prediction/dataset/Laptop_price.csv")

add_selectbox = st.sidebar.selectbox(
    
)
page = ['Dataset', 'Predict Section']

st.sidebar.('Dataset'):
    st.head()