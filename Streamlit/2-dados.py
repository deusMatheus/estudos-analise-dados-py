import pandas as pd
import numpy as np
import streamlit as st

df = pd.DataFrame(
    np.random.randn(50,20),
    columns=('col %d' %i for i in range(20))
)

st.header('Utilizando DataFrame')
st.dataframe(df)

st.header('Utilizando Table')
st.table(df)

st.header('Utilizando Métrica')
st.metric(label='Temperatura', value='70ºF', delta='1.2ºF')

st.header('Utilizando JSON')
st.json({
    'foo': 'bar',
    'bax': 'boz',
    'stuff': {
        'stuff1',
        'stuff2',
        'stuff3',
        'stuff4',
    }
})