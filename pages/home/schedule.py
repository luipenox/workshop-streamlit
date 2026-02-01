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
col1.metric("Délka", "1 den", "9:00 – 18:00")
col2.metric("Úroveň", "Začátečník / Mírně pokr.", "Python")
col3.metric("Výsledek", "Webová aplikace", "Streamlit Cloud")

st.markdown("---")

# --- Dopolední blok ---
st.header("☀️ Dopolední blok: Analýza a Vizualizace")
st.caption("Cíl: Připravit data a grafy, které budeme později prezentovat.")

render_block(
    "09:00 – 09:45", 
    "Úvod a Setup", 
    "Představení, nastavení prostředí a stažení dat.", 
    "👋", 
    "theory"
)

render_block(
    "09:45 – 10:00", 
    "Coffee Break", 
    "Ranní káva.", 
    "☕", 
    "break"
)

render_block(
    "10:00 – 11:15", 
    "Pandas: Jak zkrotit data", 
    "Načtení CSV, průzkum dat, čištění a filtrace. Praktický úkol.", 
    "🐼", 
    "practice"
)

render_block(
    "11:15 – 11:30", 
    "Coffee Break", 
    "Krátká pauza.", 
    "🥐", 
    "break"
)

render_block(
    "11:30 – 12:30", 
    "Vizualizace: Hledáme příběh", 
    "Tvorba interaktivních grafů pomocí Altair (Bar, Line, Scatter).", 
    "📊", 
    "practice"
)

render_block(
    "12:30 – 13:30", 
    "Oběd", 
    "Zasloužená pauza na jídlo.", 
    "🍽️", 
    "break"
)

st.markdown("---")

# --- Odpolední blok ---
st.header("🌙 Odpolední blok: Streamlit a Deployment")
st.caption("Cíl: Sestavit aplikaci, přidat interaktivitu a zveřejnit ji.")

render_block(
    "13:30 – 14:45", 
    "Ahoj, Streamlite!", 
    "Základní struktura aplikace, zobrazení textů a grafů, layout.", 
    "🚀", 
    "practice"
)

render_block(
    "14:45 – 15:00", 
    "Coffee Break", 
    "Odpolední káva.", 
    "🍩", 
    "break"
)

render_block(
    "15:00 – 16:15", 
    "Interaktivita", 
    "Práce s widgety (selectbox, slider) a jejich propojení s filtrováním dat.", 
    "🎛️", 
    "practice"
)

render_block(
    "16:15 – 16:30", 
    "Coffee Break", 
    "Poslední pauza.", 
    "🥤", 
    "break"
)

render_block(
    "16:30 – 17:15", 
    "Finalizace a Cachování", 
    "Optimalizace výkonu, postranní panel a ladění designu.", 
    "🎨", 
    "practice"
)

render_block(
    "17:15 – 18:00",
    "Jdeme online", 
    "Vytvoření requirements.txt, push na GitHub a nasazení na Streamlit Cloud.", 
    "☁️", 
    "theory"
)
