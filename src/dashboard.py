import streamlit as st
import pandas as pd
import altair as alt

# Nastavení stránky
st.set_page_config(page_title="Můj Dashboard", layout="wide")

# Funkce pro načtení dat
@st.cache_data
def load_data():
    df = pd.read_csv('../data/prodeje.csv')
    df['Datum'] = pd.to_datetime(df['Datum'])
    df['Celkem'] = df['Cena'] * df['Mnozstvi']
    return df

st.title("📊 Můj první Streamlit Dashboard")

# Načtení dat
try:
    df = load_data()
    st.success("Data úspěšně načtena!")
except FileNotFoundError:
    st.error("Soubor s daty nebyl nalezen.")
    st.stop()

# Sidebar - Filtry
st.sidebar.header("Filtry")
selected_category = st.sidebar.multiselect(
    "Vyber kategorii",
    options=df['Kategorie'].unique(),
    default=df['Kategorie'].unique()
)

# Filtrace dat
filtered_df = df[df['Kategorie'].isin(selected_category)]

# Zobrazení dat
st.subheader("Náhled dat")
st.dataframe(filtered_df.head())

# Metriky
total_sales = filtered_df['Celkem'].sum()
st.metric("Celkové tržby", f"{total_sales:,.0f} Kč")

# Grafy
st.subheader("Vizualizace")

# Altair Bar Chart
chart = alt.Chart(filtered_df).mark_bar().encode(
    x='Kategorie',
    y='sum(Celkem)',
    color='Pobocka',
    tooltip=['Kategorie', 'sum(Celkem)']
).interactive()

st.altair_chart(chart, use_container_width=True)
