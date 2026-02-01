import streamlit as st
import pandas as pd
import altair as alt
import datetime

# --- Konfigurace ---
st.set_page_config(layout="wide")

# --- Hlavní nadpis ---
st.title("🎛️ Interaktivita Masterclass")
st.caption("Nechte uživatele, ať si s daty hrají.")

# --- Navigace ---
tab_principle, tab_widgets, tab_filter, tab_state, tab_challenge = st.tabs([
    "1. Princip", 
    "2. Katalog widgetů", 
    "3. Filtrování dat", 
    "4. Session State", 
    "🚀 IMPLEMENTACE"
])

# ==========================================
# TAB 1: PRINCIP
# ==========================================
with tab_principle:
    st.header("🔄 Jak fungují widgety?")
    st.markdown("""
    Ve Streamlitu je widget jen funkce, která **vrací hodnotu**.
    
    *   Když uživatel pohne posuvníkem, Streamlit spustí skript znovu.
    *   Funkce widgetu vrátí novou hodnotu.
    *   Tuto hodnotu uložíte do proměnné a použijete dál v kódu.
    """)
    
    st.code("""
# 1. Vytvoříme widget a uložíme výsledek do proměnné
jmeno = st.text_input("Jak se jmenuješ?")

# 2. Použijeme proměnnou
st.write(f"Ahoj {jmeno}!")
    """, language="python")
    
    st.divider()
    
    # Živá ukázka
    col1, col2 = st.columns(2)
    with col1:
        jmeno = st.text_input("Jak se jmenuješ?", key="demo_name")
    with col2:
        if jmeno:
            st.success(f"Ahoj **{jmeno}**! 👋")
        else:
            st.info("Napiš něco vlevo...")

# ==========================================
# TAB 2: KATALOG WIDGETŮ
# ==========================================
with tab_widgets:
    st.header("🎛️ Katalog widgetů")
    st.markdown("To nejlepší, co Streamlit nabízí.")

    # 1. Výběry
    st.subheader("1. Výběry (Selection)")
    c1, c2 = st.columns(2)
    with c1:
        st.code('st.selectbox("Vyber", ["A", "B"])', language="python")
        st.selectbox("Vyber jednu možnost", ["Možnost A", "Možnost B"], key="sb")
    with c2:
        st.code('st.multiselect("Vyber", ["A", "B"])', language="python")
        st.multiselect("Vyber více možností", ["A", "B", "C"], default=["A"], key="ms")

    st.divider()

    # 2. Čísla a Posuvníky
    st.subheader("2. Čísla a Posuvníky")
    c1, c2 = st.columns(2)
    with c1:
        st.code('st.slider("Věk", 0, 100, 25)', language="python")
        st.slider("Nastav věk", 0, 100, 25, key="sl")
    with c2:
        st.code('st.number_input("Cena", 0, 1000)', language="python")
        st.number_input("Zadej cenu", 0, 1000, 100, key="ni")

    st.divider()

    # 3. Datum a Čas
    st.subheader("3. Datum a Čas")
    c1, c2 = st.columns(2)
    with c1:
        st.code('st.date_input("Datum")', language="python")
        st.date_input("Kdy?", datetime.date.today(), key="di")
    with c2:
        st.code('st.time_input("Čas")', language="python")
        st.time_input("V kolik?", datetime.time(12, 00), key="ti")

    st.divider()

    # 4. Tlačítka
    st.subheader("4. Akce")
    c1, c2 = st.columns(2)
    with c1:
        st.code('st.button("Klikni")', language="python")
        if st.button("Klikni na mě", key="btn"):
            st.balloons()
    with c2:
        st.code('st.checkbox("Zobrazit")', language="python")
        st.checkbox("Zobrazit detaily", key="cb")

# ==========================================
# TAB 3: FILTROVÁNÍ DAT
# ==========================================
with tab_filter:
    st.header("🔍 Propojení s daty (Filtrování)")
    st.markdown("Tohle je svatý grál dashboardů. Widget ovládá Pandas filtr.")

    # Příprava dat
    df = pd.DataFrame({
        'Město': ['Praha', 'Brno', 'Ostrava', 'Praha', 'Brno'],
        'Tržba': [100, 200, 150, 300, 250]
    })

    st.subheader("Krok 1: Widget")
    st.code("""
mesta = df['Město'].unique()
vyber = st.multiselect("Vyber město:", mesta, default=mesta)
    """, language="python")
    
    mesta = df['Město'].unique()
    vyber = st.multiselect("Vyber město:", mesta, default=mesta, key="filter_demo")

    st.subheader("Krok 2: Filtrace DataFrame")
    st.code("""
# Magický řádek
filtered_df = df[df['Město'].isin(vyber)]
    """, language="python")
    
    filtered_df = df[df['Město'].isin(vyber)]

    st.subheader("Krok 3: Výsledek")
    c1, c2 = st.columns(2)
    with c1:
        st.write("Tabulka:")
        st.dataframe(filtered_df, hide_index=True)
    with c2:
        st.write("Graf:")
        st.bar_chart(filtered_df, x='Město', y='Tržba')

# ==========================================
# TAB 4: SESSION STATE
# ==========================================
with tab_state:
    st.header("🧠 Session State (Paměť)")
    st.markdown("""
    Streamlit při každém kliknutí "zapomene" proměnné, protože jede od začátku.
    Pokud si chcete něco pamatovat (např. nákupní košík), musíte použít `st.session_state`.
    """)

    st.code("""
if 'pocitadlo' not in st.session_state:
    st.session_state.pocitadlo = 0

if st.button("Přičti 1"):
    st.session_state.pocitadlo += 1

st.write(f"Hodnota: {st.session_state.pocitadlo}")
    """, language="python")

    # Demo
    if 'pocitadlo' not in st.session_state:
        st.session_state.pocitadlo = 0

    c1, c2 = st.columns([1, 4])
    with c1:
        if st.button("➕ Přičti 1", key="state_btn"):
            st.session_state.pocitadlo += 1
    with c2:
        st.metric("Počítadlo", st.session_state.pocitadlo)

# ==========================================
# TAB 5: CHALLENGE
# ==========================================
with tab_challenge:
    st.header("🚀 Implementace filtrů")
    st.markdown("Vraťte se do `src/dashboard.py` a přidejte interaktivitu.")

    st.subheader("Úkol 1: Sidebar Filtry")
    st.info("Přidejte do sidebaru `multiselect` pro výběr Pobočky a Kategorie.")
    with st.expander("Zobrazit kód"):
        st.code("""
st.sidebar.header("Filtry")

# 1. Načíst unikátní hodnoty
pobocky = df['Pobocka'].unique()

# 2. Vytvořit widget
vybrana_pobocka = st.sidebar.multiselect(
    "Vyber pobočku", 
    pobocky, 
    default=pobocky
)
        """, language="python")

    st.subheader("Úkol 2: Propojení")
    st.info("Použijte hodnotu z widgetu k filtrování hlavního DataFrame.")
    with st.expander("Zobrazit kód"):
        st.code("""
filtered_df = df[df['Pobocka'].isin(vybrana_pobocka)]

# DŮLEŽITÉ: Dále v kódu (grafy, metriky) už používejte 'filtered_df'!
        """, language="python")

    st.subheader("Úkol 3: Kontrola prázdných dat")
    st.info("Co když uživatel odškrtne všechno? Aplikace by neměla spadnout.")
    with st.expander("Zobrazit kód"):
        st.code("""
if filtered_df.empty:
    st.warning("Žádná data pro zobrazení.")
    st.stop()
        """, language="python")
