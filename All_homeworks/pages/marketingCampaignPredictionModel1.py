import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import sklearn
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score
from PIL import Image
from sklearn.preprocessing import StandardScaler
import pickle
#import shap

#import an image
image = Image.open('/Users/birsenbas/Desktop/Kodluyoruz/streamlit/marketingcampaign.jpg')
st.image(image, use_column_width=True)

#put the heading
st.write("""
## Marketign Campaign is Successful or NOT !!
	
This apps predict the **Marketing Campaign Response**!


""")

#import dataset
df = pd.read_csv("/Users/birsenbas/Desktop/Kodluyoruz/streamlit/MarketingCampaign.csv")

selectbox_list = ['Kidhome', 'Teenhome', 'NumDealsPurchases', 'NumWebPurchases',
       'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
        'Education_en', 'Marital_Status_en']

desc_selectbox_list = ["Number of small children in customer’s household", 
						"Number of teenagers in customer’s household",
						"Number of purchases made with discount",
						"Number of purchases made through company’s web site",
						"Number of purchases made using catalogue",
						"Number of purchases made directly in stores",
						"Number of visits to company’s web site in the last month"
						"Customer’s level of education",
						"Customer’s marital status"]

slidebar_list = ['Year_Birth', 'Income', 'Recency', 'MntWines',
       'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']

desc_slidebar_list = ["Birthday year", "Customer’s yearly household income", 
						"Number of days since the last purchase",
						"Amount spent on wine products in the last 2 years",
						"Amount spent on fruits products in the last 2 years",
						"Amount spent on meat products in the last 2 years",
						"Amount spent on fish products in the last 2 years",
						"Amount spent on sweet products in the last 2 years",
						"Amount spent on gold products in the last 2 years"]

box_overall_dict = {}
slider_overall_dict = {}

# Creating dictionary for value names and their descriptions
for var1, var2 in zip(selectbox_list, desc_selectbox_list):
    box_overall_dict.update({var1: var2})

for var1, var2 in zip(slidebar_list, desc_slidebar_list):
    slider_overall_dict.update({var1: var2})

print(box_overall_dict)
print(slider_overall_dict)

# Displaying box and slider with functions
def showing_box(var, desc):
        cycle_option = sorted(list(df[var].unique()))
        box = st.sidebar.selectbox(label= f"{desc}", options=cycle_option)
        return box

def showing_slider(var, desc):
        slider = st.sidebar.slider(label= f"{desc}", min_value=round(df[var].min()), max_value=round(df[var].max()))
        return slider

print(selectbox_list)
print(slidebar_list)


# Collecting user inputs in dictionaries
box_dict = {}
slider_dict = {}

for key, value in box_overall_dict.items():
    box_dict.update({key: showing_box(key, value)})

for key, value in slider_overall_dict.items():
    slider_dict.update({key: showing_slider(key, value)})

print(box_dict)
print(slider_dict)


input_dict = {**box_dict, **slider_dict}
dictf = pd.DataFrame(input_dict, index=[0])
#df = df.append(dictf, ignore_index= True) 

df.drop("Response", inplace=True,axis=1)
scaler = StandardScaler()
scaler.fit(df)
df1 = pd.DataFrame(scaler.transform(df),index = df.index,columns = df.columns)
features=pd.DataFrame(df1.iloc[[-1]])

#import model with pickle
with open('/Users/birsenbas/Desktop/Kodluyoruz/streamlit/marketing_model.sav', 'rb') as f:
    model = pickle.load(f)

#prediction
ypred = model.predict(features)
st.subheader("Marketing campaign response")
st.write(ypred)



