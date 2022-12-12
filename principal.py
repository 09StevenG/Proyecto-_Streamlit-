# Aplicación desarrollada en Streamlit para visualización de datos de biodiversidad
## Autor código fuente : Manuel Vargas (mfvargas@gmail.com)
### Estudiante que utiliza código base  : Steven Guillén Rivera 
#### Fecha de creación: 2022-12-12

# Cargar bibliotecas 

import streamlit as st 
import pandas as pd
import geopandas as gpd
import plotly.express as px
import folium
from folium import Marker
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import math

st.title('Aplicación Streamlit')

