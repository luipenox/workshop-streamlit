import streamlit as st
import pandas as pd
import altair as alt

# --- Konfigurace a Data ---
st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('data/prodeje.csv')
    df['Datum'] = pd.to_datetime(df['Datum'])
    df['Celkem'] = df['Cena'] * df['Mnozstvi']
    return df

df = load_data()

# --- Hlavní nadpis ---
st.title("📊 Altair Masterclass")
st.caption("Gramatika grafiky: Jak skládat vizualizace jako lego.")

# --- Navigace ---
tab_theory, tab_basic, tab_adv, tab_agg, tab_challenge = st.tabs([
    "1. Teorie (Gramatika)", 
    "2. Základní grafy", 
    "3. Vylepšování", 
    "4. Agregace v grafu", 
    "🚀 PŘÍPRAVA PRO DASHBOARD"
])

# ==========================================
# TAB 1: TEORIE
# ==========================================
with tab_theory:
    st.header("🧠 Grammar of Graphics")
    st.markdown("""
    Altair není o tom, že si pamatujete názvy funkcí. Je o tom, že graf **popíšete**.
    Každý graf se skládá ze 3 hlavních částí:
    """)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**1. DATA**")
        st.write("Tabulka (DataFrame), kterou chceme vizualizovat.")
    with c2:
        st.info("**2. MARK (Značka)**")
        st.write("Jak data zobrazíme? (Tečka, Čára, Sloupec...)")
    with c3:
        st.info("**3. ENCODING (Mapování)**")
        st.write("Který sloupec patří na osu X? Který na Y? Který určuje barvu?")

    st.divider()
    
    st.subheader("Syntaxe v Pythonu")
    st.code("""
alt.Chart(DATA).mark_TYP_GRAFU().encode(
    x='SLOUPEC_PRO_OSU_X',
    y='SLOUPEC_PRO_OSU_Y',
    color='SLOUPEC_PRO_BARVU'
)
    """, language="python")
    
    st.caption("Příklad: `alt.Chart(df).mark_bar().encode(x='Kategorie', y='Cena')`")

# ==========================================
# TAB 2: ZÁKLADNÍ GRAFY
# ==========================================
with tab_basic:
    st.header("📈 Základní typy grafů")
    
    # --- BAR CHART ---
    st.subheader("A) Bar Chart (Sloupcový)")
    st.markdown("Ideální pro porovnání kategorií.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
alt.Chart(df).mark_bar().encode(
    x='Kategorie',
    y='Cena'
)
        """, language="python")
    with col2:
        c = alt.Chart(df).mark_bar().encode(x='Kategorie', y='Cena')
        st.altair_chart(c, use_container_width=True)

    st.divider()

    # --- LINE CHART ---
    st.subheader("B) Line Chart (Čárový)")
    st.markdown("Ideální pro vývoj v čase.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
alt.Chart(df).mark_line().encode(
    x='Datum',
    y='Cena'
)
        """, language="python")
    with col2:
        c = alt.Chart(df).mark_line().encode(x='Datum', y='Cena')
        st.altair_chart(c, use_container_width=True)

    st.divider()

    # --- SCATTER PLOT ---
    st.subheader("C) Scatter Plot (Bodový)")
    st.markdown("Ideální pro hledání vztahů (korelace).")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
alt.Chart(df).mark_circle().encode(
    x='Mnozstvi',
    y='Cena'
)
        """, language="python")
    with col2:
        c = alt.Chart(df).mark_circle(size=60).encode(x='Mnozstvi', y='Cena')
        st.altair_chart(c, use_container_width=True)

# ==========================================
# TAB 3: VYLEPŠOVÁNÍ
# ==========================================
with tab_adv:
    st.header("🎨 Vylepšování grafů")
    st.markdown("Grafy musí být nejen správné, ale i hezké a čitelné.")

    # --- BARVY ---
    st.subheader("1. Barvy a Legenda")
    st.markdown("Přidáme `color`, aby se data rozlišila.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
alt.Chart(df).mark_circle().encode(
    x='Mnozstvi',
    y='Cena',
    color='Kategorie' # Automaticky vytvoří legendu
)
        """, language="python")
    with col2:
        c = alt.Chart(df).mark_circle(size=60).encode(
            x='Mnozstvi', y='Cena', color='Kategorie'
        )
        st.altair_chart(c, use_container_width=True)

    st.divider()

    # --- TOOLTIPY ---
    st.subheader("2. Tooltipy (Bubliny)")
    st.markdown("Co se stane, když najedete myší na bod?")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
alt.Chart(df).mark_bar().encode(
    x='Kategorie',
    y='Cena',
    tooltip=['Produkt', 'Cena', 'Datum']
)
        """, language="python")
    with col2:
        c = alt.Chart(df).mark_bar().encode(
            x='Kategorie', y='Cena', tooltip=['Produkt', 'Cena', 'Datum']
        )
        st.altair_chart(c, use_container_width=True)

    st.divider()

    # --- INTERAKTIVITA ---
    st.subheader("3. Interaktivita")
    st.markdown("Magické slůvko `.interactive()` povolí zoom a posun.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
alt.Chart(df).mark_circle().encode(
    x='Mnozstvi',
    y='Cena'
).interactive()
        """, language="python")
    with col2:
        c = alt.Chart(df).mark_circle(size=60).encode(x='Mnozstvi', y='Cena').interactive()
        st.altair_chart(c, use_container_width=True)

# ==========================================
# TAB 4: AGREGACE V GRAFU
# ==========================================
with tab_agg:
    st.header("∑ Agregace přímo v grafu")
    st.markdown("""
    Altair je chytrý. Nemusíte data seskupovat v Pandas (groupby), můžete to říct přímo grafu!
    Používá se syntaxe: `'funkce(sloupec)'`.
    """)

    # --- SUMA ---
    st.subheader("Suma (sum)")
    st.markdown("Místo mnoha malých čárek chceme jeden velký sloupec za celou kategorii.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
alt.Chart(df).mark_bar().encode(
    x='Kategorie',
    y='sum(Cena)' # Sečti Cenu pro každou Kategorii
)
        """, language="python")
    with col2:
        c = alt.Chart(df).mark_bar().encode(x='Kategorie', y='sum(Cena)')
        st.altair_chart(c, use_container_width=True)

    st.divider()

    # --- PRŮMĚR ---
    st.subheader("Průměr (mean)")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
alt.Chart(df).mark_bar().encode(
    x='Pobocka',
    y='mean(Cena)' # Průměrná cena
)
        """, language="python")
    with col2:
        c = alt.Chart(df).mark_bar().encode(x='Pobocka', y='mean(Cena)')
        st.altair_chart(c, use_container_width=True)

# ==========================================
# TAB 5: PŘÍPRAVA PRO DASHBOARD
# ==========================================
with tab_challenge:
    st.header("🚀 Příprava grafů pro Dashboard")
    st.markdown("""
    Teď si připravíme **3 klíčové grafy**, které budeme potřebovat v odpoledním bloku.
    Otevřete si svůj editor a odlaďte si kód pro tyto vizualizace.
    """)

    # 1. KATEGORICKÝ GRAF
    st.subheader("1. Kategorický graf (Bar Chart)")
    st.info("Cíl: Ukázat, kdo je nejlepší (např. která Pobočka nebo Kategorie).")
    st.markdown("""
    *   **Mark:** `mark_bar()`
    *   **X:** Kategorický sloupec (např. Pobočka)
    *   **Y:** Suma číselného sloupce (např. `sum(Celkem)`)
    *   **Color:** Stejný jako X (pro hezčí vzhled)
    """)
    with st.expander("Zobrazit vzorový kód"):
        st.code("""
graf_kategorie = alt.Chart(df).mark_bar().encode(
    x='KATEGORIE',
    y='sum(CISLO)',
    color='KATEGORIE',
    tooltip=['KATEGORIE', 'sum(CISLO)']
).interactive()
        """, language="python")

    st.divider()

    # 2. ČASOVÝ GRAF
    st.subheader("2. Časový graf (Line Chart)")
    st.info("Cíl: Ukázat vývoj v čase (Trendy).")
    st.markdown("""
    *   **Mark:** `mark_line(point=True)`
    *   **X:** Časový sloupec (Datum)
    *   **Y:** Suma číselného sloupce
    *   **Tooltip:** Datum a Hodnota
    """)
    with st.expander("Zobrazit vzorový kód"):
        st.code("""
graf_cas = alt.Chart(df).mark_line(point=True).encode(
    x='DATUM',
    y='sum(CISLO)',
    tooltip=['DATUM', 'sum(CISLO)']
).interactive()
        """, language="python")

    st.divider()

    # 3. KORELAČNÍ GRAF
    st.subheader("3. Korelační graf (Scatter Plot)")
    st.info("Cíl: Ukázat detail a vztahy mezi metrikami.")
    st.markdown("""
    *   **Mark:** `mark_circle()`
    *   **X:** Číselná metrika A (např. Množství)
    *   **Y:** Číselná metrika B (např. Cena)
    *   **Size:** Metrika C (např. Celkem)
    *   **Color:** Kategorie
    """)
    with st.expander("Zobrazit vzorový kód"):
        st.code("""
graf_scatter = alt.Chart(df).mark_circle().encode(
    x='METRIKA_A',
    y='METRIKA_B',
    size='METRIKA_C',
    color='KATEGORIE',
    tooltip=['NAZEV', 'METRIKA_A', 'METRIKA_B']
).interactive()
        """, language="python")
