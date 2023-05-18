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

df = load_data('data/clean_ismek.csv')


st.write("# Welcome to Streamlit! 👋")

# st.sidebar.success("Select a demo above.")

df_f2f = df[df['kurs_merkezi'] != 'Uzaktan Egitim'].copy()
df_f2f = df_f2f[df_f2f.duplicated()].copy()




f2f_areas = ['Bilisim Teknolojileri', 'Dil Egitimleri', 'Kisisel Gelisim Ve Egitim','Spor','Orgu Ve Ýsleme Sanatlari']

df_f2f_top5 = get_selected_info(df_f2f,'alan', f2f_areas)

df_f2f_top5_back_up = df_f2f_top5.copy()

del df_f2f_top5['hak_edilen_belge_tipi']
del df_f2f_top5['program']

# df_f2f_top3, target_mapping = label_encoding(df_f2f_top3, 'alan')

df = df_f2f_top5.copy()

df_f2f_top5, target_mapping,encode = label_encoding(df_f2f_top5, 'alan')





# st.dataframe(df_f2f_top5)





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
                    encode['yas_araligi'][yas_araligi]])] ## bu sekilde bizim X_testimze gore doldurman lazim.


print(input_list)
with open('models/ismek_alan.sav', 'rb') as f:
    model = pickle.load(f)


print(type(model.feature_names_in_))
print(len(model.feature_names_in_)) 

predict_df = pd.DataFrame(input_list, columns= model.feature_names_in_)



print(predict_df)

if st.button('Predict...'):

    ypred = model.predict(predict_df)
    y_pred_proba = model.predict_proba(predict_df)
    top_classes = np.argsort(y_pred_proba[0])[::-1][:2]
    class1 = top_classes[0]
    class2 = top_classes[1]


    target_keys1 = [key for key, value in target_mapping.items() if value == class1]
    target_keys2 = [key for key, value in target_mapping.items() if value == class2]

    st.success(f"Onerilen ilk alan : {target_keys1[0]}")
    st.success(f"Onerilen ikinci alan : {target_keys2[0]}")


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
        
    # with left_column2:
    #     predict_1 = st.selectbox(
    #         "Predict 1",
    #         df['egitim_durumu'].unique()
    #     )

    # with right_column2:
    #     predict_2 = st.selectbox(
    #         "Predict 2",
    #         df['egitim_durumu'].unique()
    #         )






# """
# kurs_merkezi_ilcesi = st.sidebar.selectbox(
#     "kurs_merkezi_ilcesi",
#     df['kurs_merkezi_ilcesi'].unique()
# )

# # Using object notation
# egitim_durumu = st.sidebar.selectbox(
#     "egitim_durumu",
#     df['egitim_durumu'].unique()
# )
# print(df.columns)

# yas_araligi = st.sidebar.selectbox(
#     "yas_araligi",
#     df['yas_araligi'].unique()
# )

# calisma_durumu = st.sidebar.selectbox(
#     "calisma_durumu",
#     df['calisma_durumu'].unique()
# )

# tercih_sebebi = st.sidebar.selectbox(
#     "tercih_sebebi",
#     df['tercih_sebebi'].unique()
# )

# """