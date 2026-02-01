import streamlit as st

st.set_page_config(layout="wide")

st.title("Použité technologie 🛠️")
st.caption("Seznamte se s nástroji, které dnes budeme používat.")

st.markdown("""
Dnešní workshop stojí na moderním **Python stacku** pro datovou analýzu. 
Vybrali jsme tyto knihovny, protože jsou standardem v oboru a skvěle spolupracují.
""")

col1, col2 = st.columns(2)

with col1:
    st.header("🐍 Python")
    st.markdown("""
    **Jazyk, který vládne datům.**
    *   Jednoduchá syntaxe (čte se jako angličtina).
    *   Obrovská komunita a ekosystém knihoven.
    *   Používá ho NASA, Netflix i Spotify.
    """)

    st.header("🐼 Pandas")
    st.markdown("""
    **Excel na steroidech.**
    *   Knihovna pro manipulaci s tabulkovými daty.
    *   Umí načíst cokoliv (CSV, Excel, SQL, JSON).
    *   Bleskurychlé filtrování, čištění a agregace milionů řádků.
    """)

with col2:
    st.header("📊 Altair")
    st.markdown("""
    **Gramatika grafiky.**
    *   Deklarativní knihovna pro vizualizaci.
    *   Neříkáte *jak* kreslit (cykly), ale *co* kreslit (data -> osy).
    *   Vytváří krásné, interaktivní grafy, které se snadno vkládají do webu.
    """)

    st.header("👑 Streamlit")
    st.markdown("""
    **Webové aplikace bez webového vývoje.**
    *   Framework, který promění Python skript v interaktivní aplikaci.
    *   Nepotřebujete znát HTML, CSS ani JavaScript.
    *   Ideální pro dashboardy, prototypy a prezentaci dat.
    """)

st.divider()

st.info("""
💡 **Proč tato kombinace?**
Pandas připraví data -> Altair je vykreslí -> Streamlit je zabalí do aplikace.
Je to nejrychlejší cesta od surových dat k hotovému produktu.
""")
