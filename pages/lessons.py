import streamlit as st

pages = [
    st.Page(
        page="pages/lessons/01_introduction.py",
        title="Úvod",
        icon=":material/counter_1:"
    ),
    st.Page(
        page="pages/lessons/02_pandas.py",
        title="Pandas",
        icon=":material/counter_2:"
    ),
    st.Page(
        page="pages/lessons/03_visualization.py",
        title="Vizualizace",
        icon=":material/counter_3:"
    ),
    st.Page(
        page="pages/lessons/04_streamlit_basics.py",
        title="Základy Streamlit",
        icon=":material/counter_4:"
    ),
    st.Page(
        page="pages/lessons/05_interactivity.py",
        title="Interaktivita",
        icon=":material/counter_5:"
    ),
    st.Page(
        page="pages/lessons/06_deployment.py",
        title="Deployment",
        icon=":material/counter_6:"
    ),
]
