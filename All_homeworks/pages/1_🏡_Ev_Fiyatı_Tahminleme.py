import streamlit as st
from datetime import time
import time
import numpy as np
import pandas as pd
import pickle
from PIL import Image

import functions

st.set_page_config(page_title="Local-House Price", page_icon="🏡")

st.markdown("# 🏡 Local-House Price")
st.sidebar.header(" 🏡 Local-House Price")
st.write("""
		## Let's Find Out the Price of Your New House !!
		\n**This project aims** to predict estimated price of a house according to given values can be related with.
       \nWe worked on a **regression problem** to find a solution.  
       \n**👈You can use estimation panel which is located on the sidebar to enter feature values of the house**
       \nFor parameter explanations visit: **[Input Parameters Explanations](https://jse.amstat.org/v19n3/decock/DataDocumentation.txt)**
	   
       """
)

st.sidebar.write('### Please select feature values of the house:')

##df1 = pd.read_csv('All_homeworks/dataSets/house_price.csv')
df1 = pd.read_csv('All_homeworks/dataSets/house_price.csv')

#columns_range_list = functions.df_columns_value_range(df1)

def user_input_features():
	MSZoning = st.sidebar.selectbox("House zone", ("RL" ,"RM" ,"FV", "RH" ,"C(all)")) 
	# RL: Residential Low Density,RM	:Residential Medium Density	
    # ,FV:	Floating Village Residential, RH	:Residential High Density,  
    # C(all) : Commercial   
	BedroomAbvGr = st.sidebar.selectbox("Bedroom", (0,1,2,3,4,5,6))
	LotShape = st.sidebar.selectbox("General shape", ("Reg", "IR1" , "IR2"  , "IR3"))
	 # Reg: Regular	, IR1:	Slightly irregular , IR2:	Moderately Irregular,IR3:	Irregular 
	LotArea = st.sidebar.slider("Lot size in sqft", 1300, 215245, 5000)
	OverallQual = st.sidebar.selectbox("Rates for material and finish house", (2, 3, 4, 5, 6, 7, 8, 9, 10))
	#  1 : Very Poor -  10: Very Excellent
	YearBuilt = st.sidebar.slider("Construction date", 1880, 2010, 1990)
	HeatingQC = st.sidebar.selectbox("Heating quality", ("Ex", "TA", "Gd", "Fa", "Po"))
    #tx1 = st.sidebar.write("Ex: Excellent, Gd:	Good, TA:	Average/Typical, Fa:	Fair, Po:	Poor")
	YearRemodAdd = st.sidebar.slider("Innovation date", 1950, 2010, 2000)
	TotalBsmtSF = st.sidebar.slider("Total sqft of basement", 105, 6110, 300)
	onestFlrSF = st.sidebar.slider("First Floor square feet ", 438, 4692, 1098) 
	GrLivArea = st.sidebar.slider("Living area sqft", 438, 5642, 700)
	FullBath = st.sidebar.selectbox("Full bathroom", (0,1,2,3))
	TotRmsAbvGrd = st.sidebar.selectbox("Total rooms above grade", (3,4,5,6,7,8,9,10,11,12))
	GarageCars = st.sidebar.selectbox("Garage car capacity", (1,2,3,4))
	GarageArea = st.sidebar.slider("Garage sqft", 160, 1418, 300)
	data = {"MSZoning":MSZoning, "BedroomAbvGr":BedroomAbvGr, "LotShape":LotShape, "LotArea":LotArea,
			"OverallQual":OverallQual, "YearBuilt":YearBuilt, "HeatingQC":HeatingQC, "YearRemodAdd":YearRemodAdd,
			"TotalBsmtSF":TotalBsmtSF, "1stFlrSF" :onestFlrSF, "GrLivArea" : GrLivArea, "FullBath":FullBath,
			"TotRmsAbvGrd":TotRmsAbvGrd, "GarageCars":GarageCars, "GarageArea":GarageArea
	       }
	features = pd.DataFrame(data,index=[0])
	return features                     
          

user_sample = user_input_features()

with st.container():
	st.subheader("Selected values of features:")
	st.write("""\n**👈You can use estimation panel which is located on the sidebar to change feature values of the house**
				\n**👇Estimated price will be appear below.**""")
	
	# CSS to inject contained in a string
	hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

	# Inject CSS with Markdown
	st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
	st.table(user_sample)


# target_encoder import and transform
f = 'All_homeworks/models/Target_Encoder.sav'
target_encoder = pickle.load(open(f, 'rb'))
user_sample_encoded= target_encoder.transform(user_sample)
user_sample_log = np.log1p(user_sample_encoded)

filename = 'All_homeworks/models/house_price_model.sav'
house_price_model = pickle.load(open(filename, 'rb'))
# predict house
prediction = house_price_model.predict(user_sample_log)


# Show Prediction result
st.success(f"###  👉 Estimated price of this house: ${int(np.round(np.exp(prediction)))}") #  #{float(np.round(prediction,2))}")

image = Image.open('All_homework/images/houseprice.jpg')
st.image(image, use_column_width=True)
