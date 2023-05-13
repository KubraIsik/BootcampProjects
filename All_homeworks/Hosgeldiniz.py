import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Hoşgeldiniz",
    page_icon="👋",
)

st.write("# Kodluyoruz Python ile Veri Bilimi Bootcamp Projeleri! 🎨")

st.sidebar.success("👆Görüntülemek İstediğiniz Projeyi Seçin")

st.markdown(
    """
    Merhaba,
    burada Kodluyoruz Veri Bilimi Bootcamp sırasında tamamladığımız projeleri görüntüleyebileceksiniz.
    
    ### Projeleri grup pikachu ile birlikte tamamladık. 
    Grup üyelerimiz : \n
    - Kübra Nazlıhan Işık [github](https://github.com/KubraIsik) [linkedin](https://www.linkedin.com/in/kubranazlihanisik/)
    - Birsen Bayat [github](https://github.com/Birsenn) [linkedin]()
    - Hamit Güner [github](https://github.com/hamitguner) [linkedin]()
    - Gizem Bakan [github](https://github.com/gizembakan) [linkedin]()
    
    **👈 Neler yaptığımızı görmek için  bir proje seçin.**
"""
)



#"""
# 1. as sidebar menu
#with st.sidebar:
#    selected = option_menu("Main Menu", ["Home", 'Settings'], 
#        icons=['house', 'gear'], menu_icon="cast", default_index=1)
#    selected

# 3. CSS style definitions
#selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
#    icons=['house', 'cloud-upload', "list-task", 'gear'], 
#    menu_icon="cast", default_index=0, orientation="horizontal",
#    styles={
#        "container": {"padding": "0!important", "background-color": "#fafafa"},
#        "icon": {"color": "orange", "font-size": "25px"}, 
#        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#        "nav-link-selected": {"background-color": "green"},
#    }
#)"""
