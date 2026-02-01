import streamlit as st

pages = [
    st.Page(
        page="pages/home/about.py",
        title="O projektu",
        icon=":material/rocket_launch:"
    ),
    st.Page(
        page="pages/home/schedule.py",
        title="Harmonogram",
        icon=":material/schedule:"
    ),
    st.Page(
        page="pages/home/contact.py",
        title="Kontakt",
        icon=":material/mail:"
    ),
]
