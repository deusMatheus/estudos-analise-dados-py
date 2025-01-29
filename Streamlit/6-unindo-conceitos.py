import streamlit as st
import pandas as pd
import altair as alt

#Carregar o conjunto de dados Iris
iris_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

st.title('Dashboard com Dados Íris')
st.write('Deste dashboard apresenta informações sobre as espécies Íris')

# Obtendo as espécies únicas de íris com seletor
species_list = iris_df['species'].unique()
selected_species = st.selectbox('Selecione a espécie de íris', species_list)

#Filtrando DF com base na espécie selecionada
filtered_data = iris_df[iris_df['species'] == selected_species]

# Criando gráfico de dispersão interativo com Altair
scatter_chart = alt.Chart(filtered_data).mark_circle().encode(
    x = 'sepal_length',
    y = 'sepal_width',
    color = 'species',
    tooltip=['species', 'sepal_length', 'sepal_width']
).properties(
    width = 600,
    height = 400
).interactive()

st.altair_chart(scatter_chart, use_container_width=True)