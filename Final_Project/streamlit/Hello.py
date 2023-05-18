import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

df = load_data('data/clean_ismek.csv')


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:

color_columns = ['Seçiniz','egitim_durumu', 'calisma_durumu', 'hak_edilen_belge_tipi','tercih_sebebi', 'yas_araligi']
# Or even better, call Streamlit functions inside a "with" block:
with left_column:
    option = st.selectbox(
    'Which number do you like best?',
    df.columns)

try:
    color_columns.remove(option)


except:
    if option not in color_columns:
        color_columns= ['Seçiniz']

# if option not in color_columns:
#     color_columns= ['None']

with right_column:
    option2 = st.selectbox(
    'Which number do you like best2?',
    color_columns)


if option2 == 'Seçiniz':
    fig = px.histogram(df, x=option).update_xaxes(categoryorder="total descending")
    st.plotly_chart(fig)

else:
    fig = px.histogram(df, x=option, color=option2, barmode='group').update_xaxes(categoryorder="total descending")
    st.plotly_chart(fig)


# sozluk= {'calisma_durumu': 'calisma durumu cok kotu'}
# sozluk[option]