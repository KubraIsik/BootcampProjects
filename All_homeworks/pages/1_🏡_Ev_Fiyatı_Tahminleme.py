import streamlit as st
from datetime import time
import time
import numpy as np
import pandas as pd
import pickle
from PIL import Image

import functions

st.set_page_config(page_title="Ev Fiyatı Tahminleme", page_icon="🏡")

st.markdown("# 🏡 Ev Fiyatı Tahminleme ")
st.sidebar.header(" 🏡 Ev Fiyatı Tahminleme ")
st.write(
    """**Amaç :** elimizdeki verilere göre eğittiğimiz model ile ev fiyatı tahminleme.
       \nBurada bir regresyon problemi üzerine çalıştık. 
       Evin konumu, garaj sayısı gibi birçok özelliğine göre bir evin sahip olabileceği olası değeri tahmin ediyoruz. 
       \n **👇Aşağıdaki tahminleme aracına istediğiniz değerleri girerek tahmin sonuçlarını 👈yanda görüntüleyebilirsiniz:**
       \nNOT: Burada predict yaptığımız tüm sütunlar için bir değer almak burayı kalabalık yapar mı? Bazı featureları default alıp
       kalan featurelar kullanıcıdan input olarak alınsa nasıl olur? predict sonuçlarını etkiler mi?
       """
)

image = Image.open('houseprice.jpg')
st.image(image, use_column_width=True)

st.write("""
## Get the Price for Your New House !!
	
This apps predict the **house prices**!

For **PARAMATER EXPLANATIONS**, please go to site: [Input Parameters Explanations](https://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

""")

st.sidebar.write(f'### Please select values of the house:')

df1 = pd.read_csv('house_price.csv')

#columns_range_list = functions.df_columns_value_range(df1)

def user_input_features():
	MSZoning = st.sidebar.selectbox("House zone", (0, 1, 2, 3, 4))
	LotShape = st.sidebar.selectbox("General shape", (0, 1, 2, 3))
	HouseStyle = st.sidebar.selectbox("House style", (0, 1, 2, 3, 4, 5, 6, 7))
	OverallQual = st.sidebar.selectbox("Rates for material and finish house", (2, 3, 4, 5, 6, 7, 8, 9, 10))
	RoofStyle = st.sidebar.selectbox("Roof style", (0, 1, 2, 3, 4, 5))
	ExterQual = st.sidebar.selectbox("Exterior material quality", (0,1,2,3))
	Foundation = st.sidebar.selectbox("Foundation type", (0,1,2,3,4))
	BsmtQual = st.sidebar.selectbox("Basement height", (0,1,2,3))
	BsmtExposure = st.sidebar.selectbox("Basement level", (0,1,2,3))
	HeatingQC = st.sidebar.selectbox("Heating quality", (0,1,2,3,4))
	BsmtFullBath = st.sidebar.selectbox("Basement full bathroom", (0,1,2))
	FullBath = st.sidebar.selectbox("Full bathroom", (0,1,2,3))
	HalfBath = st.sidebar.selectbox("Half bathroom", (0,1,2))
	BedroomAbvGr = st.sidebar.selectbox("Bedroom", (0,1,2,3,4,5,6))
	KitchenQual = st.sidebar.selectbox("Kitchen quality", (0,1,2,3))
	TotRmsAbvGrd = st.sidebar.selectbox("Total rooms above grade", (3,4,5,6,7,8,9,10,11,12))
	Fireplaces = st.sidebar.selectbox("Number of fireplaces", (0,1,2,3))
	GarageType = st.sidebar.selectbox("Garage location", (0,1,2,3,4,5))
	GarageFinish = st.sidebar.selectbox("Interior finish of the garage", (0,1,2))
	GarageCars = st.sidebar.selectbox("Garage car capacity", (1,2,3,4))
	SaleCondition = st.sidebar.selectbox("Sale condition", (0,1,2,3,4,5))
	LotArea = st.sidebar.slider("Lot size in sqft", 1300, 215245, 5000)
	Neighborhood = st.sidebar.slider("Neighborhood", 0, 24, 5)
	YearBuilt = st.sidebar.slider("Construction date", 1880, 2010, 1990)
	YearRemodAdd = st.sidebar.slider("Innovation date", 1950, 2010, 2000)
	BsmtFinSF1 = st.sidebar.slider("Finished sqft", 0, 5644, 1000)
	BsmtUnfSF = st.sidebar.slider("Unfinished basement sqft", 0, 2336, 500)
	TotalBsmtSF = st.sidebar.slider("Total sqft of basement", 105, 6110, 300)
	GrLivArea = st.sidebar.slider("Living area sqft", 438, 5642, 700)
	GarageYrBlt = st.sidebar.slider("Garage year built", 1900, 2010, 2000)
	GarageArea = st.sidebar.slider("Garage sqft", 160, 1418, 300)
	WoodDeckSF = st.sidebar.slider("Wood deck sqft", 0, 857, 300)
	OpenPorchSF = st.sidebar.slider("Open porch sqft", 0, 547, 100)
	data = {"MSZoning":MSZoning, "LotShape":LotShape, "HouseStyle":HouseStyle, "OverallQual":OverallQual, "RoofStyle":RoofStyle,
			"ExterQual":ExterQual, "Foundation":Foundation, "BsmtQual":BsmtQual, "BsmtExposure":BsmtExposure,"HeatingQC":HeatingQC,
			"BsmtFullBath":BsmtFullBath, "FullBath":FullBath, "HalfBath":HalfBath, "BedroomAbvGr":BedroomAbvGr,"KitchenQual":KitchenQual,
			"TotRmsAbvGrd":TotRmsAbvGrd, "Fireplaces":Fireplaces, "GarageType":GarageType, "GarageFinish":GarageFinish, "GarageCars":GarageCars,
			"SaleCondition":SaleCondition, "LotArea":LotArea, "Neighborhood":Neighborhood, "YearBuilt":YearBuilt, "YearRemodAdd":YearRemodAdd,
			"BsmtFinSF1":BsmtFinSF1, "BsmtUnfSF":BsmtUnfSF, "TotalBsmtSF":TotalBsmtSF, "GrLivArea" : GrLivArea, "GarageYrBlt":GarageYrBlt,
			"GarageArea":GarageArea, "WoodDeckSF":WoodDeckSF, "OpenPorchSF":OpenPorchSF,
			}
	features = pd.DataFrame(data, index=[0])
	return features                     
          

user_sample = user_input_features()

st.subheader("User Input parameters")
st.write(user_sample)


# load the house price model
filename = 'house_price_Model.sav'
house_price_model = pickle.load(open(filename, 'rb'))

prediction = house_price_model.predict(user_sample)

st.subheader('Prediction')
st.write(prediction)

# Yan tarafta sidebar da görüntüle
st.sidebar.success(f"###  👉 Ev fiyatı tahmin: ${prediction}")  


# Plot Animation
# Burada yukarıda hesaplanan prediction değerleri
# eş zamanlı olarak aşağıdaki plot a eklenip gösterilebilir mi?
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
#last_rows = np.random.randn(1, 1)
last_rows = prediction
chart = st.line_chart(last_rows)

#for i in range(1, 101):
if user_sample.any:
	new_rows = last_rows[-1] + prediction #np.random.randn(5, 1).cumsum(axis=0)
	#new_rows = prediction
		#status_text.text("%i%% Complete" % i)
	chart.add_rows(new_rows)
		#progress_bar.progress(i)
	last_rows = new_rows
time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")


# Plot Animation
#progress_bar = st.sidebar.progress(0)
#status_text = st.sidebar.empty()
#last_rows = np.random.randn(1, 1)
#chart = st.line_chart(last_rows)

#for i in range(1, 101):
#    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#    status_text.text("%i%% Complete" % i)
#    chart.add_rows(new_rows)
#    progress_bar.progress(i)
#    last_rows = new_rows
#    time.sleep(0.05)

#progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
#st.button("Re-run")


#st.sidebar.write(
#        f""" \n GrLivArea: Üstü (zemin) oturma alanı metre karesi: {age}
#            \nMSZoning: Genel imar sınıflandırması: {options}
#            \nLotFrontage: Mülkiyetin cadde ile doğrudan bağlantısının olup olmaması
#            \nLotArea: Parsel büyüklüğü
#            \nStreet: Yol erişiminin tipi
#            \nAlley: Sokak girişi tipi
#            \nLotShape: Mülkün genel şekli
#            \nBsmtQual: Bodrumun yüksekliği
#            \nYrSold: Satıldığı yıl """
#)
