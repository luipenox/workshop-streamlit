import streamlit as st

st.title("Kontakt 📬")

st.markdown("""
Máte dotazy k workshopu, materiálům nebo potřebujete pomoci s instalací?
Neváhejte se na mě obrátit.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Lektor")
    st.markdown("**Luděk Reif**")
    st.markdown("📧 Email: [luipenox@gmail.com](mailto:luipenox@gmail.com)")
    st.markdown("📞 Telefon: +420 720 116 008")

with col2:
    st.info("💡 Během workshopu se ptejte kdykoliv!")

st.divider()

st.caption("Těším se na viděnou na workshopu! 🚀")
