import plotly.graph_objs as go
import pandas as pd

data = {
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'StockA': [ i + 100 for i in range (100) ],
    'StockB': [ 120 - i for i in range (100) ],
    'StockC': [ 90  + i*0.5 for i in range (100) ]  
}

df = pd.DataFrame(data)

# Criando gráfico de linhas interativo

fig = go.Figure()
fig.add_trace(go.Scatter(
    x = df['Date'],
    y = df['StockA'],
    mode='lines',
    name='Stock A'
))
fig.add_trace(go.Scatter(
    x = df['Date'],
    y = df['StockB'],
    mode='lines',
    name='Stock B'
))
fig.add_trace(go.Scatter(
    x = df['Date'],
    y = df['StockC'],
    mode='lines',
    name='Stock C'
))

# Layout do gráfico
fig.update_layout(
    title = 'Variação de preço ao longo do tempo',
    xaxis_title = 'Data',
    yaxis_title = 'Preço',
    hovermode = 'x'
)

fig.show()