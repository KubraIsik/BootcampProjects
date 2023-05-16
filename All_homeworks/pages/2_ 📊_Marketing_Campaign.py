import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from sklearn.metrics import r2_score
from PIL import Image
from sklearn.preprocessing import StandardScaler
import pickle
import sys
import numpy as np


st.set_page_config(page_title="Marketing Campaign", page_icon="📊")

image = Image.open('All_homeworks/images/marketingcampaign.jpg')
print(image)
st.image(image, use_column_width=True)

st.markdown("# 📊 Marketing Campaign")
st.sidebar.header("📊 Marketing Campaign")
st.write(
    """## Marketign Campaign is Successful or NOT !!
        \nThis project aims to predict response of a customer according to marketing campaign features.
       \nA Classification model is created to estimate response.
       \n**👈You can use estimation panel on the left to see prediction result👇:**"""
)


#import dataset
df = pd.read_csv("All_homeworks/dataSets/MarketingCampaign.csv")


selectbox_list = ['Kidhome', 'Teenhome', 'NumDealsPurchases', 'NumWebPurchases',
       'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
        'Education_en', 'Marital_Status_en']

desc_selectbox_list = ["Number of small children in customer’s household", 
						"Number of teenagers in customer’s household",
						"Number of purchases made with discount",
						"Number of purchases made through company’s web site",
						"Number of purchases made using catalogue",
						"Number of purchases made directly in stores",
						"Number of visits to company’s web site in the last month",
						"Customer’s level of education",
						"Customer’s marital status"]

slidebar_list = ['Year_Birth', 'Income', 'Recency', 'MntWines',
       'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']#,'Dt_Customer_en']

desc_slidebar_list = ["Birthday year", "Customer’s yearly household income", 
						"Number of days since the last purchase",
						"Amount spent on wine products in the last 2 years",
						"Amount spent on fruits products in the last 2 years",
						"Amount spent on meat products in the last 2 years",
						"Amount spent on fish products in the last 2 years",
						"Amount spent on sweet products in the last 2 years",
						"Amount spent on gold products in the last 2 years"]#,
						#"Date of customer’s enrolment with the company"]
                        

box_overall_dict = {}
slider_overall_dict = {}

# Creating dictionary for value names and their descriptions
for var1, var2 in zip(selectbox_list, desc_selectbox_list):
    box_overall_dict.update({var1: var2})

for var1, var2 in zip(slidebar_list, desc_slidebar_list):
    slider_overall_dict.update({var1: var2})

#st.write(box_overall_dict)
#st.write(slider_overall_dict)

# Displaying box and slider with functions
def showing_box(var, desc):
        cycle_option = sorted(list(df[var].unique()))
        box = st.sidebar.selectbox(label= f"{desc}", options=cycle_option)
        return box

def showing_slider(var, desc):
        slider = st.sidebar.slider(label= f"{desc}", min_value=round(df[var].min()), max_value=round(df[var].max()))
        return slider

# Collecting user inputs in dictionaries
box_dict = {}
slider_dict = {}

for key, value in box_overall_dict.items():
    box_dict.update({key: showing_box(key, value)})

for key, value in slider_overall_dict.items():
    slider_dict.update({key: showing_slider(key, value)})


input_dict = {**box_dict, **slider_dict}
dictf = pd.DataFrame(input_dict, index=[0])
df = df.append(dictf, ignore_index= True) 

#st.table(input_dict)
#input_list = [tuple([input_dict['Year_Birth'],input_dict['Income']])] ## bu sekilde bizim X_testimze gore doldurman lazim.
#print(input_list)

#input_list=[input_dict['Year_Birth'], input_dict['Income'],input_dict['Kidhome'],input_dict['Teenhome'],input_dict['Recency'],
#input_dict['MntWines'],input_dict['MntFruits'],input_dict['MntMeatProducts'],input_dict['MntFishProducts'],
#input_dict['MntSweetProducts'],input_dict['MntGoldProds'],input_dict['NumDealsPurchases'],input_dict['NumWebPurchases'],
#input_dict['NumCatalogPurchases'],input_dict['NumStorePurchases'],input_dict['NumWebVisitsMonth'],input_dict['Education_en'],
#input_dict['Marital_Status_en']]

df.drop("Response", inplace=True,axis=1)
features=pd.DataFrame(df.iloc[[-1]])

#import model with pickle
with open('All_homeworks/models/marketing_model.sav', 'rb') as f:
    model = pickle.load(f)

#prediction
ypred = model.predict(features)
#st.subheader("Marketing campaign response")
#st.write(ypred)

# Show Prediction result
st.success(f"###  👉 Marketing campaign response: {ypred}")

#prediction  
#arr_f_name = model.feature_names_in_

#columns= arr_f_name[:-1].tolist() # burada -1 yaptım çünkü Dt_Customer_en i almamak için
# Dt_Customer_en datadan çıkarılıp eklenirse  [:-1] yapmaya gerek yok


#predict_df = pd.DataFrame([input_list], columns= columns,index=[0])
#st.table(predict_df)
# üstteki errorlar çözüldü.
# burada hata veriyor. Çünkü Dt_Customer_en çıkarılıp model train edilip tekrar yüklenmesi gerekiyor
# Dt_Customer_en ilk başta datadan çıkardığımız bir sürun idi.

#ypred = model.predict(predict_df)


#st.write(ypred)
#st.subheader("Marketing campaign response")
# st.write(ypred)
#response = "Yes" if ypred == 0 else "No"
#st.success(f"###  👉 This customer response or not(Yes/No):",response)  



