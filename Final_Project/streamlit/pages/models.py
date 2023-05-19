import streamlit as st
import pandas as pd
from sklearn import preprocessing
import pickle
import xgboost as xgb
import numpy as np

st.set_page_config(
    page_title="Models",
    page_icon="👺",
)


@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df


def get_selected_info(df, column, selected_list):
    new_df = pd.DataFrame()
    for col in selected_list:
        new_df = pd.concat([new_df, df[(df[column] == col)]])
        
    return new_df.reset_index(drop=True)


def label_encoding(df, target):
    encode_mapping = {}
    for i in df.columns:
        label_encoder = preprocessing.LabelEncoder()

        # Encode labels in column 'species'.
        df[i]= label_encoder.fit_transform(df[i])
        
        
        mapping = {l: i for i, l in enumerate(label_encoder.classes_)}
        encode_mapping[i] = mapping
        
        if i == target:
            target_mapping = {l: i for i, l in enumerate(label_encoder.classes_)}
            print(target_mapping) # for target
        
    return df, target_mapping ,encode_mapping

# df = load_data('data/clean_ismek.csv')
df = load_data('Final_Project/streamlit/data/clean_ismek.csv')


st.write("# Welcome to Streamlit! 👋")


df_f2f = df[df['kurs_merkezi'] != 'Uzaktan Egitim'].copy()
df_f2f = df_f2f[df_f2f.duplicated()].copy()




f2f_areas = ['Bilisim Teknolojileri', 'Dil Egitimleri', 'Kisisel Gelisim Ve Egitim','Spor','Orgu Ve Ýsleme Sanatlari']

df_f2f_top5 = get_selected_info(df_f2f,'alan', f2f_areas)

df_f2f_top5_back_up = df_f2f_top5.copy()

del df_f2f_top5['hak_edilen_belge_tipi']
del df_f2f_top5['program']



df = df_f2f_top5.copy()

df_f2f_top5, target_mapping,encode = label_encoding(df_f2f_top5, 'alan')



left_column, right_column = st.columns(2)

with left_column:
    egitim_durumu = st.selectbox(
        "egitim_durumu",
        df['egitim_durumu'].unique()
    )



with left_column:
    yas_araligi = st.selectbox(
        "yas_araligi",
        df['yas_araligi'].unique()
    )


with right_column:
    calisma_durumu = st.selectbox(
        "calisma_durumu",
        df['calisma_durumu'].unique()
    )

with right_column:
    tercih_sebebi = st.selectbox(
        "tercih_sebebi",
        df['tercih_sebebi'].unique()
    )


kurs_merkezi_ilcesi = st.selectbox(
    "kurs_merkezi_ilcesi",
    df['kurs_merkezi_ilcesi'].unique()
)

kurs_merkezi = st.selectbox(
    "kurs_merkezi",
    df[df.kurs_merkezi_ilcesi == kurs_merkezi_ilcesi].kurs_merkezi.unique()
)


input_list = [tuple([encode['egitim_durumu'][egitim_durumu],
                    encode['calisma_durumu'][calisma_durumu],
                    encode['kurs_merkezi'][kurs_merkezi],
                    encode['kurs_merkezi_ilcesi'][kurs_merkezi_ilcesi],
                    encode['tercih_sebebi'][tercih_sebebi],
                    encode['yas_araligi'][yas_araligi]])]


with open('Final_Project/streamlit/models/ismek_alan.sav', 'rb') as f:
    model = pickle.load(f)



predict_df = pd.DataFrame(input_list, columns= model.feature_names_in_)



if st.button('Predict...'):

    ypred = model.predict(predict_df)
    y_pred_proba = model.predict_proba(predict_df)
    top_classes = np.argsort(y_pred_proba[0])[::-1][:2]
    class1 = top_classes[0]
    class2 = top_classes[1]


    target_keys1 = [key for key, value in target_mapping.items() if value == class1]
    target_keys2 = [key for key, value in target_mapping.items() if value == class2]

    with open('Final_Project/streamlit/models/ismek_haketme.sav', 'rb') as f:
        model_haketme = pickle.load(f)

    class1_predict = predict_df.copy()
    class2_predict = predict_df.copy()
    class1_predict.insert(2, "alan", [class1], True)
    class2_predict.insert(2, "alan", [class2], True)



    ypred_haketme_class1 = model_haketme.predict(class1_predict)
    y_pred_proba_haketme_class1  = model_haketme.predict_proba(class1_predict) * 100

    ypred_haketme_class2 = model_haketme.predict(class2_predict)
    y_pred_proba_haketme_class2 = model_haketme.predict_proba(class2_predict) * 100


    
    st.success(f"Onerilen ilk alan : **{target_keys1[0]}** 👉👉 Sertifika alma ihtimali :**%{int(y_pred_proba_haketme_class1[:,1][0])}**")
    st.success(f"Onerilen ikinci alan : **{target_keys2[0]}** 👉👉 Sertifika alma ihtimali :**%{int(y_pred_proba_haketme_class2[:,1][0])}**")


    filter1 = df_f2f_top5_back_up['alan'] == target_keys1[0]
    filter2 = df_f2f_top5_back_up['alan'] == target_keys2[0]
    filter3 = df_f2f_top5_back_up['kurs_merkezi'] == kurs_merkezi


    programs_1 = df_f2f_top5_back_up.where(filter1 & filter3)['program'].dropna().unique()
    programs_2 = df_f2f_top5_back_up.where(filter2 & filter3)['program'].dropna().unique()


    left_column2, right_column2 = st.columns(2)

    with left_column2:
        target_keys1[0]
        programs_1
    
    with right_column2:
        target_keys2[0]
        programs_2
        
