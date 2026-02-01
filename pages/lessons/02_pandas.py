import streamlit as st
import pandas as pd
import numpy as np

# --- Konfigurace a Data ---
st.set_page_config(layout="wide")

# Funkce pro generování "špinavých" dat
@st.cache_data
def get_dirty_data():
    df = pd.read_csv('data/prodeje.csv')
    df['Datum'] = pd.to_datetime(df['Datum'])
    # Simulace chyb
    df.loc[2, 'Cena'] = np.nan          # Chybějící hodnota
    df.loc[5, 'Pobocka'] = 'brno'       # Nekonzistence
    df = pd.concat([df, df.iloc[[0]]], ignore_index=True) # Duplikát
    return df

df = get_dirty_data()
# Aplikace čištění a transformace na pozadí
df['Cena'] = df['Cena'].fillna(0)
df = df.drop_duplicates()
df['Pobocka'] = df['Pobocka'].str.capitalize()
df['Celkem'] = df['Cena'] * df['Mnozstvi']
df_clean = df.copy()

# --- Hlavní nadpis ---
st.title("🐼 Pandas Masterclass")
st.caption("Od surových dat k čistým insightům během jedné hodiny.")

# --- Navigace ---
tab_load, tab_clean, tab_transform, tab_agg, tab_challenge = st.tabs([
    "1. Načtení & Průzkum", 
    "2. Čištění dat", 
    "3. Transformace", 
    "4. Agregace (Pivot)", 
    "🚀 PŘÍPRAVA PRO GRAFY"
])

# ==========================================
# TAB 1: NAČTENÍ A PRŮZKUM
# ==========================================
with tab_load:
    st.header("🔍 Průzkum dat: Krok za krokem")
    st.markdown("Když dostanete nová data, chováte se jako detektiv. Musíte zjistit, s čím máte tu čest.")

    # --- KROK 1: Import a Načtení ---
    st.subheader("Krok 1: Import a Načtení")
    st.markdown("Nejdřív musíme knihovnu importovat a načíst soubor (CSV, Excel).")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
import pandas as pd

# Načtení CSV souboru do proměnné 'df' (DataFrame)
df = pd.read_csv('data/prodeje.csv')
        """, language="python")
    with col2:
        st.success("Data načtena do paměti RAM.")
        st.write("Proměnná `df` nyní obsahuje celou tabulku.")

    st.divider()

    # --- KROK 2: První pohled (Head/Tail) ---
    st.subheader("Krok 2: První pohled (`head`)")
    st.markdown("Nikdy nevypisujte celou tabulku (`print(df)`), pokud má milion řádků. Podívejte se jen na začátek.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("df.head() # Zobrazí prvních 5 řádků", language="python")
        st.caption("Existuje i `df.tail()`, která ukáže konec tabulky.")
    with col2:
        st.dataframe(df.head())

    st.divider()

    # --- KROK 3: Rozměry (Shape) ---
    st.subheader("Krok 3: Kolik toho je? (`shape`)")
    st.markdown("Základní otázka: Mám 10 řádků nebo 10 milionů?")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("df.shape", language="python")
        st.caption("Vrátí (počet_řádků, počet_sloupců)")
    with col2:
        shape = df.shape
        st.write(f"**Výsledek:** {shape}")
        st.info(f"Máme **{shape[0]}** záznamů a **{shape[1]}** sloupců.")

    st.divider()

    # --- KROK 4: Struktura a Typy (`info`) ---
    st.subheader("Krok 4: Technická kontrola (`info`)")
    st.markdown("Jsou čísla opravdu čísla? Je datum datum? A nechybí nám něco?")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("df.info()", language="python")
        st.markdown("""
        **Co hledat:**
        *   `Dtype`: Je 'Cena' `int/float`? (Pokud je `object`, je to špatně).
        *   `Non-Null Count`: Pokud je číslo menší než počet řádků, chybí data!
        """)
    with col2:
        import io
        buffer = io.StringIO()
        df.info(buf=buffer)
        st.text(buffer.getvalue())

    st.divider()

    # --- KROK 5: Statistiky (`describe`) ---
    st.subheader("Krok 5: Matematický pohled (`describe`)")
    st.markdown("Rychlý přehled o číselných sloupcích. Odhalí extrémy a divné hodnoty.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("df.describe()", language="python")
        st.markdown("""
        **Vysvětlivky:**
        *   `mean`: Průměr
        *   `min/max`: Extrémy (nejsou tam záporné ceny?)
        *   `50%`: Medián (často lepší než průměr)
        """)
    with col2:
        st.dataframe(df.describe())

    st.divider()

    # --- KROK 6: Kategorická data (`value_counts`) ---
    st.subheader("Krok 6: Co je ve sloupcích? (`value_counts`)")
    st.markdown("Pro textové sloupce (Kategorie, Pobočka) nás zajímá, jaké hodnoty se tam opakují.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("df['Kategorie'].value_counts()", language="python")
    with col2:
        st.write(df['Kategorie'].value_counts())

# ==========================================
# TAB 2: ČIŠTĚNÍ DAT
# ==========================================
with tab_clean:
    st.header("🧹 Čištění dat: Diagnóza a Léčba")
    st.markdown("Data jsou málokdy dokonalá. Ukážeme si postup: **Najít problém -> Opravit problém**.")

    # --- PROBLÉM 1: Chybějící hodnoty ---
    st.subheader("1. Chybějící hodnoty (NaN)")
    st.markdown("Někdy data prostě chybí. Pandas je označuje jako `NaN` (Not a Number).")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🕵️ Diagnóza: Kde to chybí?**")
        st.code("df.isnull().sum()", language="python")
        st.write("Výsledek:", df.isnull().sum())
        st.warning("Vidíme, že ve sloupci 'Cena' chybí 1 hodnota.")
    
    with col2:
        st.markdown("**💊 Léčba: Doplnit nebo smazat?**")
        st.markdown("Můžeme řádek smazat (`dropna`) nebo doplnit (`fillna`). Zde doplníme nulu.")
        st.code("df['Cena'] = df['Cena'].fillna(0)", language="python")
        
        # Aplikace opravy
        df['Cena'] = df['Cena'].fillna(0)
        st.success("Hotovo! Počet NaN nyní: " + str(df['Cena'].isnull().sum()))

    st.divider()

    # --- PROBLÉM 2: Duplicity ---
    st.subheader("2. Duplicity")
    st.markdown("Stejný řádek se v datech objeví dvakrát (např. chyba při exportu).")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🕵️ Diagnóza: Máme dvojčata?**")
        st.code("df.duplicated().sum()", language="python")
        dups = df.duplicated().sum()
        st.write(f"Počet duplicitních řádků: **{dups}**")
        if dups > 0:
            st.warning("Pozor, máme tam duplicity!")
    
    with col2:
        st.markdown("**💊 Léčba: Odstranit duplicity**")
        st.code("df = df.drop_duplicates()", language="python")
        
        # Aplikace opravy
        df = df.drop_duplicates()
        st.success(f"Hotovo! Počet duplicit nyní: {df.duplicated().sum()}")

    st.divider()

    # --- PROBLÉM 3: Nekonzistentní text ---
    st.subheader("3. Nekonzistentní text (Překlepy)")
    st.markdown("Počítač vidí 'Brno' a 'brno' jako dvě různé věci.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🕵️ Diagnóza: Co tam máme?**")
        st.code("df['Pobocka'].unique()", language="python")
        st.write("Unikátní hodnoty:", df['Pobocka'].unique())
        st.warning("Vidíte 'Brno' a 'brno'?")
    
    with col2:
        st.markdown("**💊 Léčba: Sjednotit velikost**")
        st.markdown("Převedeme vše na formát 'První velké'.")
        st.code("df['Pobocka'] = df['Pobocka'].str.capitalize()", language="python")
        
        # Aplikace opravy
        df['Pobocka'] = df['Pobocka'].str.capitalize()
        st.success("Hotovo! Hodnoty: " + str(df['Pobocka'].unique()))

# ==========================================
# TAB 3: TRANSFORMACE
# ==========================================
with tab_transform:
    st.header("🛠️ Feature Engineering: Tvorba nových dat")
    st.markdown("Surová data často nestačí. Musíme si 'vypočítat' to, co nás zajímá.")

    # --- 1. Matematické operace ---
    st.subheader("1. Matematické operace")
    st.markdown("Máme `Cenu` a `Množství`. Chceme vědět, kolik zákazník zaplatil celkem.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("df['Celkem'] = df['Cena'] * df['Mnozstvi']", language="python")
    with col2:
        df_clean['Celkem'] = df_clean['Cena'] * df_clean['Mnozstvi']
        st.dataframe(df_clean[['Produkt', 'Cena', 'Mnozstvi', 'Celkem']].head(3))

    st.divider()

    # --- 2. Práce s časem (Datetime) ---
    st.subheader("2. Práce s časem (Datetime)")
    st.markdown("Datum `2023-01-01` nám moc neřekne. Ale 'Leden' nebo 'Neděle' už ano!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
# Měsíc (slovně)
df['Mesic'] = df['Datum'].dt.month_name()

# Den v týdnu
df['Den'] = df['Datum'].dt.day_name()
        """, language="python")
    with col2:
        df_clean['Mesic'] = df_clean['Datum'].dt.month_name()
        df_clean['Den'] = df_clean['Datum'].dt.day_name()
        st.dataframe(df_clean[['Datum', 'Mesic', 'Den']].head(3))
        st.info("💡 Funguje jen, pokud je sloupec převeden na `datetime`!")

    st.divider()

    # --- 3. Kategorizace (Binning) ---
    st.subheader("3. Kategorizace (Binning)")
    st.markdown("Chceme rozdělit objednávky na 'Malé' a 'Velké'.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
# Funkce pro kategorizaci
def obarvit(cena):
    if cena > 10000:
        return 'Velká'
    else:
        return 'Malá'

df['Typ'] = df['Celkem'].apply(obarvit)
        """, language="python")
    with col2:
        df_clean['Typ'] = df_clean['Celkem'].apply(lambda x: 'Velká' if x > 10000 else 'Malá')
        st.dataframe(df_clean[['Celkem', 'Typ']].head(3))

    st.divider()

    # --- 4. Pokročilé filtrování ---
    st.subheader("4. Pokročilé filtrování")
    st.markdown("Jak vybrat přesně to, co hledáme?")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Podmínka A ZÁROVEŇ (AND `&`)**")
        st.code("""
# Pobočka Praha A Velká objednávka
mask = (df['Pobocka'] == 'Praha') & (df['Typ'] == 'Velká')
df[mask]
        """, language="python")
    with col2:
        mask = (df_clean['Pobocka'] == 'Praha') & (df_clean['Typ'] == 'Velká')
        st.dataframe(df_clean[mask].head(3))

# ==========================================
# TAB 4: AGREGACE
# ==========================================
with tab_agg:
    st.header("📊 Agregace: Od detailu k přehledu")
    st.markdown("Manažera nezajímají jednotlivé účtenky. Zajímá ho: **'Kolik jsme vydělali v Praze?'**")

    # --- 1. GroupBy (Základ) ---
    st.subheader("1. GroupBy (Seskupování)")
    st.markdown("Princip: Rozděl data do skupinek -> Spočítej něco pro každou skupinku.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Příklad: Tržby podle Pobočky**")
        st.code("""
# Seskupit podle 'Pobocka' a sečíst 'Celkem'
df.groupby('Pobocka')['Celkem'].sum()
        """, language="python")
    with col2:
        res = df_clean.groupby('Pobocka')['Celkem'].sum()
        st.dataframe(res)

    st.divider()

    # --- 2. Více metrik najednou ---
    st.subheader("2. Více metrik najednou (.agg)")
    st.markdown("Co když chci součet, průměr i počet objednávek najednou?")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
df.groupby('Kategorie')['Celkem'].agg(
    ['sum', 'mean', 'count']
)
        """, language="python")
    with col2:
        res_agg = df_clean.groupby('Kategorie')['Celkem'].agg(['sum', 'mean', 'count'])
        st.dataframe(res_agg)

    st.divider()

    # --- 3. Řazení výsledků ---
    st.subheader("3. Řazení výsledků (.sort_values)")
    st.markdown("Chceme vidět ty nejlepší nahoře.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
# Seřadit sestupně (ascending=False)
df.groupby('Pobocka')['Celkem'].sum().sort_values(ascending=False)
        """, language="python")
    with col2:
        res_sort = df_clean.groupby('Pobocka')['Celkem'].sum().sort_values(ascending=False)
        st.dataframe(res_sort)

    st.divider()

    # --- 4. Pivot Tables (Kontingenční tabulky) ---
    st.subheader("4. Pivot Tables (Matice)")
    st.markdown("Královská disciplína. Data ve dvou dimenzích (řádky vs. sloupce).")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
df.pivot_table(
    values='Celkem',    # Co počítáme (čísla)
    index='Pobocka',    # Co je v řádcích
    columns='Kategorie',# Co je ve sloupcích
    aggfunc='sum',      # Funkce (sum, mean...)
    fill_value=0        # Co dát místo NaN
)
        """, language="python")
    with col2:
        pivot = df_clean.pivot_table(
            values='Celkem', 
            index='Pobocka', 
            columns='Kategorie', 
            aggfunc='sum',
            fill_value=0
        )
        st.dataframe(pivot)

# ==========================================
# TAB 5: PŘÍPRAVA PRO GRAFY (OBECNĚ)
# ==========================================
with tab_challenge:
    st.header("🚀 Příprava podkladů pro Dashboard")
    st.markdown("""
    Ať už analyzujete prodeje, počasí nebo sportovní výsledky, vždy budete potřebovat připravit data pro grafy.
    Zde je **5 univerzálních vzorů**, které využijete v 90 % případů.
    """)

    # 1. Časová řada
    st.subheader("1. Vzor: Vývoj v čase (Time Series)")
    st.info("Cíl: Připravit data pro **Line Chart**.")
    st.markdown("""
    **Princip:** Seskupit data podle časové jednotky (den, měsíc, rok) a sečíst hodnoty.
    *   **X osa:** Časový sloupec
    *   **Y osa:** Číselný sloupec (Suma/Průměr)
    """)
    with st.expander("Obecný vzor kódu"):
        st.code("df.groupby('CASOVY_SLOUPEC')['CISELNY_SLOUPEC'].sum().reset_index()", language="python")

    st.divider()

    # 2. Kategorické srovnání
    st.subheader("2. Vzor: Žebříček (Ranking)")
    st.info("Cíl: Připravit data pro **Bar Chart**.")
    st.markdown("""
    **Princip:** Seskupit data podle kategorie a seřadit je, abychom viděli "Kdo je nejlepší".
    *   **X osa:** Kategorický sloupec (Kdo?)
    *   **Y osa:** Číselný sloupec (Kolik?)
    """)
    with st.expander("Obecný vzor kódu"):
        st.code("""
df.groupby('KATEGORICKY_SLOUPEC')['CISELNY_SLOUPEC'].sum()
  .sort_values(ascending=False)
  .reset_index()
        """, language="python")

    st.divider()

    # 3. Detailní rozpad
    st.subheader("3. Vzor: Rozpad (Drill-down)")
    st.info("Cíl: Připravit data pro **Stacked Bar Chart**.")
    st.markdown("""
    **Princip:** Seskupit data podle DVOU kategorií najednou.
    *   **X osa:** Hlavní kategorie (např. Pobočka)
    *   **Barva:** Podkategorie (např. Typ produktu)
    *   **Y osa:** Číselný sloupec
    """)
    with st.expander("Obecný vzor kódu"):
        st.code("df.groupby(['HLAVNI_KAT', 'POD_KAT'])['CISELNY_SLOUPEC'].sum().reset_index()", language="python")

    st.divider()

    # 4. Korelace
    st.subheader("4. Vzor: Vztahy (Correlation)")
    st.info("Cíl: Připravit data pro **Scatter Plot**.")
    st.markdown("""
    **Princip:** Zde většinou neagregujeme. Hledáme vztah mezi dvěma čísly na úrovni detailu.
    *   **X osa:** Číselný sloupec A (např. Cena)
    *   **Y osa:** Číselný sloupec B (např. Množství)
    """)
    with st.expander("Obecný vzor kódu"):
        st.code("df[['CISELNY_SLOUPEC_A', 'CISELNY_SLOUPEC_B', 'KATEGORIE']]", language="python")

    st.divider()

    # 5. KPI Metriky
    st.subheader("5. Vzor: Jedno číslo (KPI)")
    st.info("Cíl: Připravit data pro **Big Number**.")
    st.markdown("""
    **Princip:** Jednoduchá agregace celého sloupce. Žádné seskupování.
    """)
    with st.expander("Obecný vzor kódu"):
        st.code("total = df['CISELNY_SLOUPEC'].sum()", language="python")
