import streamlit as st

st.title("kur hesaplama")


bitcoin_fiyati =3.606.797,24 

st.info(f"Güncel BTC Kuru: {bitcoin_fiyati:,} TL")

btc = st.number_input("Dönüştürülecek BTC miktarını girin:", min_value=0.0, format="%.6f")

if btc > 0:
    sonuc = btc * bitcoin_fiyati
    st.success(f"Sonuç: {sonuc:,.2f} TL")
