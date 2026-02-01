import streamlit as st

st.title("🛠️ Instalace a Prostředí")
st.markdown("Abychom mohli začít programovat a nakonec aplikaci zveřejnit, musíme si připravit 'kuchyni'.")

# --- 1. PYTHON ---
st.header("1. Python (Lokální vývoj)")
st.markdown("""
Pro vývoj Streamlit aplikace (odpolední blok) potřebujeme Python u sebe na počítači.
*   [Stáhnout Python](https://www.python.org/downloads/) (verze 3.8+)
*   ⚠️ **Důležité:** Při instalaci na Windows zaškrtněte **"Add Python to PATH"**!
""")

st.divider()

# --- 2. EDITOR KÓDU (IDE) ---
st.header("2. Editor kódu (IDE)")
st.markdown("Místo, kde budeme psát kód. Doporučujeme jeden z těchto dvou:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("PyCharm Community")
    st.markdown("Skvělý pro začátečníky i profíky. Má spoustu věcí 'v krabici'.")
    st.link_button("Stáhnout PyCharm", "https://www.jetbrains.com/pycharm/download/")

with col2:
    st.subheader("VS Code")
    st.markdown("Lehký, rychlý a velmi populární editor od Microsoftu.")
    st.link_button("Stáhnout VS Code", "https://code.visualstudio.com/")

st.divider()

# --- 3. GIT (Verzování) ---
st.header("3. Git (Verzování)")
st.markdown("""
Nezbytný nástroj pro ukládání historie kódu a nahrávání na GitHub.
*   [Stáhnout Git](https://git-scm.com/downloads)
*   Při instalaci stačí vše odklikat (Next, Next...).
""")

st.divider()

# --- 4. ÚČTY (Registrace) ---
st.header("4. Online účty")
st.markdown("Abychom mohli aplikaci nasadit na internet, budeme potřebovat tyto dva účty:")

c1, c2 = st.columns(2)
with c1:
    st.subheader("GitHub")
    st.markdown("Zde bude uložený váš kód.")
    st.link_button("Registrovat na GitHub", "https://github.com/join")
with c2:
    st.subheader("Streamlit Cloud")
    st.markdown("Zde poběží vaše aplikace. Přihlaste se přes GitHub.")
    st.link_button("Registrovat na Streamlit", "https://share.streamlit.io/signup")

st.divider()

# --- 5. GOOGLE COLAB (Volitelné) ---
st.header("5. Google Colab (Cloud)")
st.markdown("""
Pro **dopolední část (Pandas, Altair)** můžete využít Google Colab, pokud nechcete instalovat Python hned.
Běží v prohlížeči a nic se neinstaluje.
""")
st.warning("⚠️ Pro odpolední část (Streamlit) ale budeme potřebovat lokální Python, Git a editor.")
st.link_button("Otevřít Google Colab", "https://colab.research.google.com/")

st.divider()

# --- 6. KNIHOVNY ---
st.header("6. Instalace knihoven")
st.markdown("Pro tento workshop budeme potřebovat následující balíčky.")

st.subheader("Postup:")
st.markdown("1. Otevřete terminál (v PyCharmu nebo VS Code).")
st.markdown("2. (Doporučeno) Vytvořte si virtuální prostředí:")
st.code("""
# Windows
python -m venv .venv
.venv\\Scripts\\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
""", language="bash")

st.markdown("3. Nainstalujte knihovny:")
st.code("""
pip install streamlit pandas altair openpyxl
""", language="bash")

st.info("💡 Pokud máte soubor `requirements.txt`, stačí napsat: `pip install -r requirements.txt`")
