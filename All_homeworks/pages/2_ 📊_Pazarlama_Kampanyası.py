import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from sklearn.metrics import r2_score
from PIL import Image
from sklearn.preprocessing import StandardScaler
import pickle

st.set_page_config(page_title="Pazarlama Kampanyası", page_icon="📊")

st.markdown("# 📊 Pazarlama Kampanyası")
st.sidebar.header("📊 Pazarlama Kampanyası")
st.write(
    """Pazarlama Kampanyası geri dönüşlerini tahmin etmeyi amaçlıyor.
       \nSınıflandırma modeli üzerinde çalışılmıştır.
       \nMüşteri profillerine göre pazarlama kampanyasına geri dönüş yapıp yapmamaları sınıflandırılmıştır.
       \n**👇Aşağıdaki tahminleme aracına istediğiniz sonuçları girerek tahmin sonuçlarını görüntüleyebilirsiniz👈:**"""
)

image = Image.open('All_homeworks/pages/marketingcampaign.jpg')
st.image(image, use_column_width=True)

#put the heading
st.write("""
## Marketign Campaign is Successful or NOT !!
	
This apps predict the **Marketing Campaign Response**!


""")

#import dataset
df = pd.read_csv("All_homeworks/pages/MarketingCampaign.csv")

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
       'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds','Dt_Customer_en']

desc_slidebar_list = ["Birthday year", "Customer’s yearly household income", 
						"Number of days since the last purchase",
						"Amount spent on wine products in the last 2 years",
						"Amount spent on fruits products in the last 2 years",
						"Amount spent on meat products in the last 2 years",
						"Amount spent on fish products in the last 2 years",
						"Amount spent on sweet products in the last 2 years",
						"Amount spent on gold products in the last 2 years",
						"Date of customer’s enrolment with the company"]

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
df = df.append(dictf, ignore_index= True) 

df.drop("Response", inplace=True,axis=1)
scaler = StandardScaler()
scaler.fit(df)
df1 = pd.DataFrame(scaler.transform(df),index = df.index,columns = df.columns)
features=pd.DataFrame(df1.iloc[[-1]])

#import model with pickle
with open('All_homeworks/pages/marketing_model_dosyasi.model', 'rb') as f:
    model = pickle.load(f)

#prediction
ypred = model.predict(features)
st.subheader("Marketing campaign response")
st.write(ypred)



# [`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)

st.sidebar.success(f"###  👉 Bu müşteri geri dönüş yapar mı(Evet/Hayır):")  

### Farklı input alma yöntemleri
#age = st.slider('GrLivArea: Üstü (zemin) oturma alanı metre karesi', 0, 130, 25)
#st.write("I'm ", age, 'years old')

#values = st.slider(
#    'MSZoning: Genel imar sınıflandırması',
#    0.0, 100.0, (25.0, 75.0))
#st.write('Values:', values)

#options = st.multiselect(
    #'MSZoning: Genel imar sınıflandırması',
    #['Evet', 'Yellow', 'Red', 'Blue'],
    #['Yellow', 'Red'])

#st.write('You selected:', options)

#number = st.number_input('Insert a number')
#st.write('The current number is ', number)


##############################
# Mapping yapan bir script
#@st.cache_data
#def from_data_file(filename):
#    url = (
#        "http://raw.githubusercontent.com/streamlit/"
#        "example-data/master/hello/v1/%s" % filename
#    )
#    return pd.read_json(url)


#try:
#    ALL_LAYERS = {
#        "Bike Rentals": pdk.Layer(
#            "HexagonLayer",
#            data=from_data_file("bike_rental_stats.json"),
#            get_position=["lon", "lat"],
#            radius=200,
#            elevation_scale=4,
#            elevation_range=[0, 1000],
#            extruded=True,
#        ),
#        "Bart Stop Exits": pdk.Layer(
#            "ScatterplotLayer",
#            data=from_data_file("bart_stop_stats.json"),
#            get_position=["lon", "lat"],
#            get_color=[200, 30, 0, 160],
#            get_radius="[exits]",
#            radius_scale=0.05,
#        ),
#        "Bart Stop Names": pdk.Layer(
#            "TextLayer",
#            data=from_data_file("bart_stop_stats.json"),
#            get_position=["lon", "lat"],
#            get_text="name",
#            get_color=[0, 0, 0, 200],
#            get_size=15,
#            get_alignment_baseline="'bottom'",
#        ),
#        "Outbound Flow": pdk.Layer(
#            "ArcLayer",
#            data=from_data_file("bart_path_stats.json"),
#            get_source_position=["lon", "lat"],
#            get_target_position=["lon2", "lat2"],
#            get_source_color=[200, 30, 0, 160],
#            get_target_color=[200, 30, 0, 160],
#            auto_highlight=True,
#            width_scale=0.0001,
#            get_width="outbound",
#            width_min_pixels=3,
#            width_max_pixels=30,
#        ),
#    }
#    st.sidebar.markdown("### Map Layers")
#    selected_layers = [
#        layer
#        for layer_name, layer in ALL_LAYERS.items()
#        if st.sidebar.checkbox(layer_name, True)
#    ]
#    if selected_layers:
#        st.pydeck_chart(
#            pdk.Deck(
#                map_style="mapbox://styles/mapbox/light-v9",
#                initial_view_state={
#                    "latitude": 37.76,
#                    "longitude": -122.4,
#                    "zoom": 11,
#                    "pitch": 50,
#                },
#                layers=selected_layers,
#            )
#        )
#    else:
#        st.error("Please choose at least one layer above.")
#except URLError as e:
#    st.error(
#        """
#        **This demo requires internet access.**
#        Connection error: %s
#    """
#        % e.reason
#    )
