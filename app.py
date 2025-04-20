import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv('C:/Users/rober/OneDrive/Escritorio/sprint_7/sprint_7_proyect/vehicles_us.csv')

st.header("Used cars analysis")

# --- PRIMER BOTÓN: Histograma ---
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# --- SEGUNDO BOTÓN: Gráfico de dispersión ---
scatter_button = st.button('Construir gráfico de dispersión') # nuevo botón

if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para precio vs odómetro')
    
    # crear el scatter plot
    fig_scatter = px.scatter(car_data, 
                            x="odometer", 
                            y="price",
                            title="Relación Precio vs Millaje",
                            labels={"odometer": "Millaje (km/mi)", "price": "Precio (USD)"},
                            hover_data=["model_year"]) # información adicional
    
    # mostrar el gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)