import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff

# Line chart
st.header('Gráfico Line Chart')
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)
# ------------------------------
# Surface area chart
st.header('Gráfico Área Chart')
st.area_chart(chart_data)
# ------------------------------
# Bar char
st.header('Gráfico Bar Char')
st.bar_chart(chart_data)
# ------------------------------
# Scatter plot
st.header('Scatterplot')
df = pd.DataFrame(
    np.random.randn(1000,2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)
# ------------------------------
# Matplotlib
st.header('Gráfico Matplotlib')
arr = np.random.normal(1,1,size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)
# ------------------------------
# Altair
st.header('Gráfico Altair')
df = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)
c = alt.Chart(df).mark_circle().encode(
    x = 'a',
    y = 'b', 
    size = 'c',
    color = 'c',
    tooltip = ['a', 'b', 'c']
)
st.altair_chart(c, use_container_width=True)
# ------------------------------
# Plotly
st.header("Gráfico Plotly")

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)
# ------------------------------