import streamlit as st

st.title("💾 Výběr dat")
st.markdown("""
Nemáte vlastní data? Nevadí! Tady je pár tipů na zajímavé veřejné zdroje, které můžete použít pro svou analýzu.
""")

st.info("💡 **Tip:** Pro tento workshop jsme pro vás připravili cvičný dataset `data/prodeje.csv`, takže nemusíte nic stahovat, pokud nechcete.")

st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("🌍 Světová data")
    st.markdown("**[Kaggle Datasets](https://www.kaggle.com/datasets)**")
    st.caption("Obrovská databáze všeho možného. Nutná registrace.")
    st.markdown("""
    *   [Titanic](https://www.kaggle.com/c/titanic/data) (Kdo přežil?)
    *   [Netflix Movies](https://www.kaggle.com/shivamb/netflix-shows) (Co sledovat?)
    *   [Airbnb NYC](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data) (Ceny ubytování)
    """)

with c2:
    st.subheader("🇨🇿 Česká data")
    st.markdown("**[Data.gov.cz](https://data.gov.cz/)**")
    st.caption("Oficiální otevřená data ČR.")
    st.markdown("""
    *   [Dopravní nehody](https://data.gov.cz/datová-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatové-sady%2F00007064%2F853503930)
    *   [Volby](https://www.volby.cz/opendata/opendata.htm)
    *   [ČSÚ (Statistiky)](https://www.czso.cz/csu/czso/otevrena_data) (Mzdy, Inflace)
    """)

with c3:
    st.subheader("📈 Statistiky")
    st.markdown("**[Our World in Data](https://ourworldindata.org/)**")
    st.caption("Kvalitní globální statistiky v CSV.")
    st.markdown("""
    *   [CO2 a Klima](https://github.com/owid/co2-data)
    *   [Energie](https://github.com/owid/energy-data)
    *   [Populace](https://ourworldindata.org/population-growth)
    """)
