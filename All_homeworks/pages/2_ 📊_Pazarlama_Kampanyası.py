import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError

st.set_page_config(page_title="Pazarlama Kampanyası", page_icon="📊")

st.markdown("# 📊 Pazarlama Kampanyası")
st.sidebar.header("📊 Pazarlama Kampanyası")
st.write(
    """Pazarlama Kampanyası geri dönüşlerini tahmin etmeyi amaçlıyor.
       \nSınıflandırma modeli üzerinde çalışılmıştır.
       \nMüşteri profillerine göre pazarlama kampanyasına geri dönüş yapıp yapmamaları sınıflandırılmıştır.
       \n**👇Aşağıdaki tahminleme aracına istediğiniz sonuçları girerek tahmin sonuçlarını görüntüleyebilirsiniz👈:**"""
)

# [`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)

st.sidebar.success(f"###  👉 Bu müşteri geri dönüş yapar mı(Evet/Hayır):")  

### Farklı input alma yöntemleri
age = st.slider('GrLivArea: Üstü (zemin) oturma alanı metre karesi', 0, 130, 25)
st.write("I'm ", age, 'years old')

#values = st.slider(
#    'MSZoning: Genel imar sınıflandırması',
#    0.0, 100.0, (25.0, 75.0))
#st.write('Values:', values)

options = st.multiselect(
    'MSZoning: Genel imar sınıflandırması',
    ['Evet', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

number = st.number_input('Insert a number')
st.write('The current number is ', number)


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