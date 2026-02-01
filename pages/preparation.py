import streamlit as st

pages = [
    st.Page(
        page="pages/preparation/install.py",
        title="Instalace",
        icon=":material/build:"
    ),
    st.Page(
        page="pages/preparation/data.py",
        title="Výběr dat",
        icon=":material/database:"
    ),
]
