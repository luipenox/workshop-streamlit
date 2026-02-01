import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# --- Konfigurace ---
st.set_page_config(layout="wide")

# --- Hlavní nadpis ---
st.title("👑 Streamlit Masterclass")
st.caption("Od prázdného skriptu k webové aplikaci za pár minut.")

# --- Navigace ---
tab_principle, tab_text, tab_layout, tab_data, tab_challenge = st.tabs([
    "1. Princip fungování", 
    "2. Texty a Prvky", 
    "3. Layout (Rozložení)", 
    "4. Data a Grafy", 
    "🚀 STAVBA APLIKACE"
])

# ==========================================
# TAB 1: PRINCIP
# ==========================================
with tab_principle:
    st.header("🔄 Jak to funguje?")
    st.markdown("""
    Streamlit je jiný než klasické webové frameworky (Django, Flask).
    
    1.  **Je to jen Python skript:** Píšete kód shora dolů.
    2.  **Magický Rerun:** Kdykoliv se něco změní (kliknete na tlačítko), **celý skript se spustí znovu od začátku**.
    3.  **Žádné HTML/CSS:** Všechny vizuální prvky jsou Python funkce.
    """)
    
    st.info("💡 **Tip:** Protože se skript spouští pořád dokola, musíme si dávat pozor na výkon (viz `@st.cache_data` později).")

    st.divider()
    
    st.subheader("Minimální aplikace")
    st.code("""
import streamlit as st

st.title("Ahoj světe!")
st.write("Tohle je moje první aplikace.")
    """, language="python")

# ==========================================
# TAB 2: TEXTY A PRVKY
# ==========================================
with tab_text:
    st.header("📝 Texty a Základní prvky")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Nadpisy")
        st.code("""
st.title("Hlavní nadpis")
st.header("Nadpis sekce")
st.subheader("Podnadpis")
        """, language="python")
        st.title("Hlavní nadpis")
        st.header("Nadpis sekce")
        st.subheader("Podnadpis")

    with col2:
        st.subheader("Formátování")
        st.code("""
st.write("Obyčejný text")
st.markdown("**Tučně**, *kurzíva*, [odkaz](...)")
st.info("Informační box")
st.success("Úspěch!")
st.error("Chyba!")
        """, language="python")
        st.write("Obyčejný text")
        st.markdown("**Tučně**, *kurzíva*")
        st.info("Informační box")
        st.success("Úspěch!")
        st.error("Chyba!")

    st.divider()
    
    st.subheader("📊 Metriky (KPI)")
    st.markdown("Skvělé pro dashboardy.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.code('st.metric("Tržby", "1M", "+10%")', language="python")
        st.metric("Tržby", "1 000 000 Kč", "+10%")
    with c2:
        st.code('st.metric("Teplota", "24°C", "-2°C")', language="python")
        st.metric("Teplota", "24 °C", "-2 °C")
    with c3:
        st.code('st.metric("Status", "OK")', language="python")
        st.metric("Status", "OK")

# ==========================================
# TAB 3: LAYOUT
# ==========================================
with tab_layout:
    st.header("📐 Layout: Jak to poskládat")
    st.markdown("Aby aplikace nevypadala jako dlouhá nudle, musíme ji strukturovat.")

    # --- COLUMNS ---
    st.subheader("1. Sloupce (`st.columns`)")
    st.code("""
col1, col2 = st.columns(2)

with col1:
    st.write("Vlevo")

with col2:
    st.write("Vpravo")
    """, language="python")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("Vlevo")
    with c2:
        st.warning("Vpravo")

    st.divider()

    # --- TABS ---
    st.subheader("2. Záložky (`st.tabs`)")
    st.code("""
tab1, tab2 = st.tabs(["Grafy", "Data"])

with tab1:
    st.write("Tady bude graf")

with tab2:
    st.write("Tady bude tabulka")
    """, language="python")
    
    t1, t2 = st.tabs(["Grafy", "Data"])
    with t1:
        st.write("📈 Graf...")
    with t2:
        st.write("📋 Tabulka...")

    st.divider()

    # --- SIDEBAR ---
    st.subheader("3. Postranní panel (`st.sidebar`)")
    st.markdown("Ideální pro filtry a nastavení.")
    st.code("""
st.sidebar.header("Filtry")
st.sidebar.write("Tohle je vlevo.")
    """, language="python")
    st.info("Podívejte se doleva! (V této demo aplikaci už sidebar je).")

    st.divider()

    # --- EXPANDER ---
    st.subheader("4. Expander (Rozbalovátko)")
    st.code("""
with st.expander("Klikni pro více info"):
    st.write("Tady je schovaný text.")
    """, language="python")
    with st.expander("Klikni pro více info"):
        st.write("Tady je schovaný text.")

# ==========================================
# TAB 4: DATA A GRAFY
# ==========================================
with tab_data:
    st.header("📈 Zobrazení Dat")
    
    # Data pro ukázku
    df_demo = pd.DataFrame({
        'Kategorie': ['A', 'B', 'C'],
        'Hodnota': [10, 20, 30]
    })

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Tabulky (`dataframe`)")
        st.markdown("Interaktivní tabulka. Můžeme skrýt index pro čistší vzhled.")
        st.code("""
# Zobrazení bez indexu (0, 1, 2...)
st.dataframe(df, hide_index=True)
        """, language="python")
        st.dataframe(df_demo, hide_index=True)
        
    with col2:
        st.subheader("Grafy (`altair_chart`)")
        st.markdown("Vložení Altair grafu.")
        st.code("""
chart = alt.Chart(df).mark_bar().encode(...)
st.altair_chart(chart, use_container_width=True)
        """, language="python")
        
        c = alt.Chart(df_demo).mark_bar().encode(x='Kategorie', y='Hodnota')
        st.altair_chart(c, use_container_width=True)

# ==========================================
# TAB 5: CHALLENGE
# ==========================================
with tab_challenge:
    st.header("🚀 Stavba kostry aplikace")
    st.markdown("""
    Teď začneme stavět váš dashboard! Otevřete si soubor `src/dashboard.py` a vytvořte základní layout.
    """)

    st.subheader("Krok 1: Konfigurace a Nadpis")
    st.info("Nastavte aplikaci na 'wide' mode a dejte jí nadpis.")
    with st.expander("Zobrazit kód"):
        st.code("""
import streamlit as st

st.set_page_config(layout="wide", page_title="Můj Dashboard")
st.title("📊 Manažerský přehled")
        """, language="python")

    st.subheader("Krok 2: Rozložení (Metriky)")
    st.info("Vytvořte 3 sloupce pro KPI metriky (zatím s fiktivními čísly).")
    with st.expander("Zobrazit kód"):
        st.code("""
col1, col2, col3 = st.columns(3)
col1.metric("Tržby", "0 Kč")
col2.metric("Objednávky", "0")
col3.metric("Průměr", "0 Kč")
        """, language="python")

    st.subheader("Krok 3: Rozložení (Grafy)")
    st.info("Vytvořte dvě záložky: 'Trendy' a 'Data'.")
    with st.expander("Zobrazit kód"):
        st.code("""
tab1, tab2 = st.tabs(["Trendy", "Data"])

with tab1:
    st.write("Tady budou grafy")

with tab2:
    st.write("Tady bude tabulka")
        """, language="python")
