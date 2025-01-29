import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.header("Botão")

if st.button('Mensagem'):
	st.write('Olá mundo')
else:
	st.write('Adeus')

st.header("Botão de Download")

@st.cache
def convert_df(df):
	return df.to_csv().encode('utf-8')

my_large_df = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

csv = convert_df(my_large_df)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )

st.header("Utilizando Checkbox")

aceito = st.checkbox('Eu aceito o termo de uso')

if aceito:
	st.write("Parabéns por ter lido os termos de uso")
else:
	st.write("Leia os termos de uso")

st.header("Utilizando RadioBox")

genero = st.radio(
     "Qual seu gênero de filme preferido",
     ('Comedia', 'Drama', 'Documentario'))

if genero == 'Comedia':
	st.write('Você selecionou gênero comédia.')
else:
	st.write("Você não gosta de filme comédia")
 
st.header("Utilizando SelectBox")
opcao = st.selectbox(
     'Escolha a opção para entrar em contato',
     ('Email', 'Fone Residencial', 'Fone Celular'))

st.write('Você selecionou:', opcao)

st.header("Utilizando MultiSelect")

opcoes = st.multiselect(
     'Qual suas cores preferidas',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('Você selecionou:', opcoes)

st.header("Utilizando o Slider")

idade = st.slider('Quantos anos você tem?', 0, 100, 25)
st.write("Eu tenho ", idade, ' anos de idade')

st.header("Utilizando o Select Slider")

cor = st.select_slider(
     'Selecione a cor',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', cor)

st.header("Input Text")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.header("Number Input")

number = st.number_input('Insert a number')
st.write('The current number is ', number)

txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
st.write('Texto:', txt)

st.header("Utilizando Date Input")

d = st.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

st.header("Utilizando o Time Input")

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)

st.header("Utilizando o File Uploader")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)

st.header("Utilizando a Câmera Input")

picture = st.camera_input("Take a picture")

if picture:
	st.image(picture)

st.header("Color Picker")

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)