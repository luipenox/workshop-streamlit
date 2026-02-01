import streamlit as st

st.title("Od dat k webové aplikaci 🚀")
st.subheader("Intenzivní workshop Pythonu a Streamlitu")

st.markdown("""
Vítejte! Tento projekt vznikl jako podklad pro jednodenní workshop, jehož cílem je naučit vás **přetavit data v interaktivní webovou aplikaci**.
Zapomeňte na posílání excelovských tabulek e-mailem. Naučíme se tvořit moderní dashboardy, které žijí na internetu.
""")

st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Co budeme tvořit?")
    st.markdown("""
    Naším cílem je vytvořit **Manažerský Dashboard prodejů**. 
    
    Během workshopu projdeme celým procesem:
    1.  **Analýza dat:** Načteme surová data o prodejích (CSV).
    2.  **Vizualizace:** Vytvoříme interaktivní grafy (Altair).
    3.  **Aplikace:** Vše zabalíme do aplikace pomocí Streamlitu.
    4.  **Deployment:** Výsledek nasadíme na veřejnou URL adresu.
    """)
    
    st.info("💡 Na konci dne budete mít vlastní portfolio projekt běžící online.")

with col2:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
    st.markdown("""
    **Použité technologie:**
    *   🐍 **Python** (jazyk)
    *   🐼 **Pandas** (data)
    *   📊 **Altair** (grafy)
    *   👑 **Streamlit** (web)
    *   🐙 **Git & GitHub** (verzování)
    """)

st.divider()

st.header("Pro koho je workshop určen?")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 👶 Začátečníci")
    st.write("Znáte základy Pythonu (proměnné, cykly), ale nikdy jste nedělali web ani pokročilou analytiku.")

with c2:
    st.markdown("### 📊 Analytici")
    st.write("Pracujete v Excelu/PowerBI a chcete posunout své schopnosti směrem k Pythonu a automatizaci.")

with c3:
    st.markdown("### 💻 Vývojáři")
    st.write("Znáte Python, ale chcete se naučit rychle prototypovat UI bez znalosti HTML/CSS/JS.")

st.divider()

st.header("Co potřebujete?")
st.warning("""
*   Nainstalovaný **Python 3.8+**
*   Editor kódu (**VS Code** nebo PyCharm)
*   Účet na **GitHubu**
*   *Volitelně:* Účet na Google (pro **Google Colab**)
""")

st.markdown("---")
st.caption("Vytvořeno pro vzdělávací účely. Materiály jsou volně dostupné.")
