import streamlit as st

st.title("Harmonogram Workshopu 🗓️")

# --- Pomocná funkce pro vykreslení bloku ---
def render_block(time, title, description, icon, type="theory"):
    """
    type: 'theory' (modrá), 'practice' (zelená), 'break' (oranžová)
    """
    
    # Barvičky a štítky podle typu
    if type == "theory":
        tag_color = "blue"
        tag_text = "📘 TEORIE"
    elif type == "practice":
        tag_color = "green"
        tag_text = "💻 PRAXE"
    else: # break
        tag_color = "orange"
        tag_text = "☕ PAUZA"

    with st.container(border=True):
        c1, c2 = st.columns([1, 4])
        
        with c1:
            st.markdown(f"### {time}")
            st.markdown(f":{tag_color}[**{tag_text}**]")
        
        with c2:
            st.subheader(f"{icon} {title}")
            st.write(description)

# --- Úvodní info ---
col1, col2, col3 = st.columns(3)
col1.metric("Délka", "1 den", "7h čistého času")
col2.metric("Úroveň", "Začátečník / Mírně pokr.", "Python")
col3.metric("Výsledek", "Webová aplikace", "Streamlit Cloud")

st.markdown("---")

# --- Dopolední blok ---
st.header("☀️ Dopolední blok: Analýza a Vizualizace")
st.caption("Cíl: Připravit data a grafy, které budeme později prezentovat.")

render_block(
    "0:00 – 0:30", 
    "Úvod a Setup", 
    "Představení, nastavení VS Code, virtuálního prostředí a stažení dat.", 
    "👋", 
    "theory"
)

render_block(
    "0:30 – 1:30", 
    "Pandas: Jak zkrotit data", 
    "Načtení CSV, průzkum dat (.info, .describe), čištění a filtrace. Praktický úkol na analýzu.", 
    "🐼", 
    "practice"
)

render_block(
    "1:30 – 1:45", 
    "Coffee Break", 
    "Doplnění kofeinu a protažení.", 
    "🥐", 
    "break"
)

render_block(
    "1:45 – 2:45", 
    "Vizualizace: Hledáme příběh", 
    "Tvorba interaktivních grafů pomocí Altair (Bar, Line, Scatter).",
    "📊", 
    "practice"
)

render_block(
    "2:45 – 3:30", 
    "Příprava logiky aplikace", 
    "Přechod od Jupyter Notebooku k .py skriptům. Strukturování kódu do funkcí.", 
    "⚙️", 
    "theory"
)

st.markdown("---")

# --- Odpolední blok ---
st.header("🌙 Odpolední blok: Streamlit a Deployment")
st.caption("Cíl: Sestavit aplikaci, přidat interaktivitu a zveřejnit ji.")

render_block(
    "0:00 – 0:45", 
    "Ahoj, Streamlite!", 
    "Základní struktura aplikace, zobrazení textů a grafů, layout (sloupce, záložky).", 
    "🚀", 
    "practice"
)

render_block(
    "0:45 – 1:45", 
    "Interaktivita", 
    "Práce s widgety (selectbox, slider) a jejich propojení s filtrováním dat.", 
    "🎛️", 
    "practice"
)

render_block(
    "1:45 – 2:00", 
    "Coffee Break", 
    "Krátká pauza před finále.", 
    "🍩", 
    "break"
)

render_block(
    "2:00 – 2:45", 
    "Finalizace a Cachování", 
    "Optimalizace výkonu (@st.cache_data), postranní panel (sidebar) a ladění designu.", 
    "🎨", 
    "practice"
)

render_block(
    "2:45 – 3:30", 
    "Jdeme online", 
    "Vytvoření requirements.txt, push na GitHub a nasazení na Streamlit Cloud.", 
    "☁️", 
    "theory"
)
