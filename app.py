import streamlit as st

from score import calcola_score
from strategy import scegli_strategia
from risk_manager import controlla_rischio
from strikes import seleziona_strike

st.set_page_config(
    page_title="SPX 0DTE Assistant",
    layout="centered"
)

st.title("SPX 0DTE Assistant")

st.write("Analisi giornaliera del mercato")

# INPUT MERCATO

vix = st.number_input(
    "VIX",
    min_value=0.0,
    value=18.0
)

trend = st.selectbox(
    "Trend",
    ["positivo", "neutro", "negativo"]
)

sopra_vwap = st.selectbox(
    "Prezzo sopra VWAP",
    ["si", "no"]
)

evento_macro = st.selectbox(
    "Evento macro importante",
    ["no", "si"]
)

range_normale = st.selectbox(
    "Range normale",
    ["si", "no"]
)

gex = st.selectbox(
    "GEX",
    ["positivo", "neutro", "negativo"]
)

capitale = st.number_input(
    "Capitale disponibile",
    value=100000
)


if st.button("ANALIZZA GIORNATA"):

    risultato_score = calcola_score(
        vix,
        trend,
        sopra_vwap == "si",
        evento_macro == "si",
        range_normale == "si",
        gex
    )

    risultato_strategia = scegli_strategia(
        risultato_score["score"],
        trend,
        sopra_vwap == "si",
        vix,
        range_normale == "si",
        gex
    )

    rischio = controlla_rischio(
        capitale,
        0.5,
        400
    )

    st.divider()

    st.subheader("RISULTATO")

    st.write(
        "Score:",
        risultato_score["score"],
        "/100"
    )

    st.write(
        "Stato:",
        risultato_score["stato"]
    )

    st.write(
        "Strategia:",
        risultato_strategia["strategia"]
    )

    st.write(
        "Motivazione:",
        risultato_strategia["motivazione"]
    )

    st.write(
        "Risk Manager:",
        rischio["stato"]
    )
