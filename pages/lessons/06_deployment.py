import streamlit as st

# --- Konfigurace ---
st.set_page_config(layout="wide")

# --- Hlavní nadpis ---
st.title("🚀 Deployment Masterclass")
st.caption("Dostaňte svou aplikaci z localhostu do světa.")

# --- Navigace ---
tab_req, tab_git, tab_cloud, tab_secrets = st.tabs([
    "1. Requirements.txt", 
    "2. GitHub", 
    "3. Streamlit Cloud", 
    "4. Secrets (Tajné)"
])

# ==========================================
# TAB 1: REQUIREMENTS
# ==========================================
with tab_req:
    st.header("📦 Krok 1: Seznam ingrediencí")
    st.markdown("""
    Když vaříte podle receptu, potřebujete seznam surovin. 
    Server (Streamlit Cloud) to má stejně. Potřebuje vědět, jaké knihovny nainstalovat.
    To mu řekneme souborem `requirements.txt`.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Jak má vypadat?")
        st.code("""
streamlit
pandas
altair
openpyxl
        """, language="text")
        st.info("Každá knihovna na nový řádek. Žádné čárky.")

    with col2:
        st.subheader("Kde má být?")
        st.warning("Musí být v **hlavní složce** (root) vašeho projektu! Vedle `app.py` nebo `dashboard.py`.")
        st.markdown("📂 `muj-projekt/`")
        st.markdown("├── 📄 `dashboard.py`")
        st.markdown("└── 📄 `requirements.txt` ✅")

# ==========================================
# TAB 2: GITHUB
# ==========================================
with tab_git:
    st.header("🐙 Krok 2: GitHub")
    st.markdown("""
    Streamlit Cloud neumí číst soubory z vašeho počítače. Musíte je nahrát na GitHub.
    """)

    st.subheader("Postup (přes webový prohlížeč)")
    
    steps = [
        "Jděte na **[github.com/new](https://github.com/new)**.",
        "Pojmenujte repozitář (např. `muj-dashboard`).",
        "Zaškrtněte **Add a README file** (doporučeno).",
        "Klikněte **Create repository**.",
        "Klikněte na **Add file** -> **Upload files**.",
        "Přetáhněte tam své soubory (`dashboard.py`, `requirements.txt`, složku `data`).",
        "Dole klikněte na zelené **Commit changes**."
    ]
    
    for i, step in enumerate(steps, 1):
        st.markdown(f"**{i}.** {step}")

    st.success("🎉 Teď máte kód v cloudu!")

# ==========================================
# TAB 3: STREAMLIT CLOUD
# ==========================================
with tab_cloud:
    st.header("☁️ Krok 3: Streamlit Cloud")
    st.markdown("Teď propojíme GitHub se Streamlitem.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Postup")
        st.markdown("""
        1.  Jděte na **[share.streamlit.io](https://share.streamlit.io)**.
        2.  Přihlaste se přes GitHub.
        3.  Klikněte na **New app**.
        4.  Vyberte svůj repozitář (`muj-dashboard`).
        5.  **Main file path:** Změňte na `src/dashboard.py` (pokud ho máte ve složce src).
        6.  Klikněte **Deploy**! 🚀
        """)
    
    with col2:
        st.subheader("Co se děje na pozadí?")
        st.info("""
        1.  Streamlit si stáhne váš kód.
        2.  Přečte `requirements.txt`.
        3.  Nainstaluje knihovny (Pandas, Altair...).
        4.  Spustí `streamlit run dashboard.py`.
        """)

    st.divider()
    st.subheader("🚑 Řešení problémů (Troubleshooting)")
    with st.expander("Aplikace spadla (Error)"):
        st.write("**1. ModuleNotFoundError:** Zapomněli jste knihovnu v `requirements.txt`.")
        st.write("**2. FileNotFoundError:** Máte špatně cestu k datům. Na Linuxu (Cloud) záleží na velkých/malých písmenech!")
        st.write("**3. Chyba v cestě:** Zkuste `data/prodeje.csv` místo `../data/prodeje.csv` (záleží, odkud se skript spouští).")

# ==========================================
# TAB 4: SECRETS
# ==========================================
with tab_secrets:
    st.header("🔐 Secrets (Tajné údaje)")
    st.markdown("""
    **Nikdy** nedávejte hesla (API klíče, hesla k databázi) přímo do kódu na GitHub!
    Každý by je viděl. Použijte **Streamlit Secrets**.
    """)

    st.subheader("Jak na to?")
    st.markdown("1. V nastavení aplikace na Streamlit Cloud klikněte na **Settings** -> **Secrets**.")
    st.markdown("2. Zadejte hesla ve formátu TOML:")
    
    st.code("""
db_username = "admin"
db_password = "moje_tajne_heslo"
    """, language="toml")

    st.markdown("3. V kódu je pak načtete takto:")
    st.code("""
import streamlit as st

user = st.secrets["db_username"]
heslo = st.secrets["db_password"]
    """, language="python")
