import streamlit as st
import pandas as pd
import altair as alt

# --- 1. Konfigurace stránky ---
st.set_page_config(
    page_title="Manažerský Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- 2. Načtení dat ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('../data/prodeje.csv')
        df['Datum'] = pd.to_datetime(df['Datum'])
        if 'Celkem' not in df.columns:
            df['Celkem'] = df['Cena'] * df['Mnozstvi']
        return df
    except FileNotFoundError:
        return None

df = load_data()

if df is None:
    st.error("Chyba: Soubor '../data/prodeje.csv' nebyl nalezen.")
    st.stop()

# --- 3. Sidebar (Filtry) ---
st.sidebar.header("Filtry")

all_branches = df['Pobocka'].unique()
selected_branch = st.sidebar.multiselect("Vyber Pobočku", all_branches, default=all_branches)

all_categories = df['Kategorie'].unique()
selected_category = st.sidebar.multiselect("Vyber Kategorii", all_categories, default=all_categories)

filtered_df = df[
    (df['Pobocka'].isin(selected_branch)) &
    (df['Kategorie'].isin(selected_category))
]

# --- 4. Hlavní obsah ---
st.title("📊 Přehled prodejů (Altair)")

if filtered_df.empty:
    st.warning("Žádná data pro zobrazení.")
    st.stop()

# KPI
total_sales = filtered_df['Celkem'].sum()
total_qty = filtered_df['Mnozstvi'].sum()
avg_order = filtered_df['Celkem'].mean()

c1, c2, c3 = st.columns(3)
c1.metric("Celkové tržby", f"{total_sales:,.0f} Kč".replace(",", " "))
c2.metric("Prodané kusy", f"{total_qty}")
c3.metric("Průměrná objednávka", f"{avg_order:.0f} Kč")

st.markdown("---")

# Grafy
tab1, tab2 = st.tabs(["📈 Trendy", "📋 Data"])

with tab1:
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Tržby dle kategorií")
        # Altair Bar Chart
        chart_bar = alt.Chart(filtered_df).mark_bar().encode(
            x=alt.X('Kategorie', sort='-y'),
            y=alt.Y('sum(Celkem)', title='Tržby'),
            color='Pobocka',
            tooltip=['Kategorie', 'sum(Celkem)', 'Pobocka']
        ).interactive()
        st.altair_chart(chart_bar, use_container_width=True)
        
    with col_chart2:
        st.subheader("Vývoj v čase")
        # Altair Line Chart
        chart_line = alt.Chart(filtered_df).mark_line(point=True).encode(
            x='Datum',
            y=alt.Y('sum(Celkem)', title='Tržby'),
            tooltip=['Datum', 'sum(Celkem)']
        ).interactive()
        st.altair_chart(chart_line, use_container_width=True)

with tab2:
    st.dataframe(filtered_df)
