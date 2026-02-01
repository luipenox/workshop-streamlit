import streamlit as st
from pages import home, lessons, preparation

st.set_page_config(layout="wide", page_title="Streamlit Workshop")

pg = st.navigation(
    {
        "Informace": home.pages,
        "Příprava": preparation.pages,
        "Kapitoly": lessons.pages
    }
)

pg.run()
