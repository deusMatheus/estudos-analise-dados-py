import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importando os Dados
data = pd.read_csv("projeto-dashboard/data/Pedidos.csv")
df = pd.DataFrame(data)

def main():
    st.title('Dashboard de vendas :shopping_trolley:')
    aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

    with aba1:
        display_df(df)

    with aba2:
        display_charts(df)

    with aba3:
        display_metrics(df)

# Função para exibir gráficos
def display_charts(data):
    st.header('Visualização de Gráficos')
#    st.set_option("deprecation.showPyplotGlobalUse", False)
#    deprecation.showPyplotGlobalUse deixou de ser utilizado em versões posteriores às aulas do streamlit

    # Gráfico 1 - desempenho x região
    st.subheader('Desempenho por Região')
    plt.figure(figsize=(10,6))
    sns.countplot(x='Regiao', data=data)
    st.pyplot()

    # Gráfico 2 - itens mais vendidos
    st.subheader('Itens mais vendidos')
    plt.figure(figsize=(10,6))
    sns.countplot(x='Item', data=data)
    st.pyplot()

    # Gráfico 3 - preço médio por item
    avg_price = data.groupby('Item')['PrecoUnidade'].mean().sort_values(ascending = False)
    st.write(avg_price)

# Função para exibir DF
def display_df(data):
    st.header('Visualização do DataFrame')
    st.sidebar.header('Filtros')
    selected_region = st.sidebar.multiselect(
        'Selecione as regiões',
        data['Regiao'].unique(),
        data['Regiao'].unique(),
    )
    filtered_data = data[data['Regiao'].isin(selected_region)]
    st.write(filtered_data)

# Função para exibir métricas
def display_metrics(data):
    st.subheader('Métricas')

    # Métricas simples
    total_sales = data['Unidades'].sum()
    average_price = data['PrecoUnidade'].mean()
    most_productive = data['Vendedor'].value_counts().idxmax()

    coluna1, coluna2, coluna3 = st.columns(3)

    with coluna1:
        st.metric('O vendedor mais produtivo: ', most_productive)

    with coluna2:
        st.metric('Vendas totais: ', total_sales)

    with coluna3:
        st.metric('Preço médio: ', round(average_price,2))

# Execução do aplicativo
if __name__ == '__main__':
    main()