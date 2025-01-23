import seaborn as sns
import plotly.express as px

data = sns.load_dataset('diamonds')

fig = px.scatter(
    data,
    x = 'carat',
    y = 'price',
    color = 'cut',
    size = 'depth',
    hover_data=['x','y'],
    title='Dispersão de Diamantes: Quilate x Preço'
)

fig.show()