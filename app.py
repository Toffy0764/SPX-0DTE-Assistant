import streamlit as st

from score import calcola_score
from strategy import scegli_strategia
from risk_manager import controlla_rischio
from strikes import seleziona_strike
from vwap import analizza_vwap
from macro import controlla_evento_macro
from adjustment import adatta_trade
from decision import genera_decisione
from trend import analizza_trend


st.set_page_config(
    page_title="SPX 0DTE Assistant",
    layout="centered"
)

st.title("📈 SPX 0DTE Assistant")


# =========================
# INPUT MERCATO
# =========================

st.subheader("📊 Dati mercato")

spx = st.number_input(
    "SPX attuale",
    value=6500
)

vwap = st.number_input(
    "VWAP giornata",
    value=6480
)

vix = st.number_input(
    "VIX",
    value=18.0
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
    [
        "positivo",
        "neutro",
        "negativo"
    ]
)


# =========================
# PREZZI TEST
# =========================

prezzi_test = [
    spx - 20,
    spx - 15,
    spx - 10,
    spx - 5,
    spx
]


# =========================
# TREND ENGINE v1.7
# =========================

risultato_trend = analizza_trend(
    prezzi_test,
    vwap
)


trend = risultato_trend["trend"]


# =========================
# RISCHIO
# =========================

st.subheader("🛡 Gestione rischio")


capitale = st.number_input(
    "Capitale disponibile",
    value=100000
)


profilo = st.selectbox(
    "Profilo rischio",
    [
        "Conservativo (0,25%)",
        "Moderato (0,50%)",
        "Bilanciato (0,75%)",
        "Dinamico (1%)"
    ]
)


if profilo == "Conservativo (0,25%)":
    rischio_percentuale = 0.25

elif profilo == "Moderato (0,50%)":
    rischio_percentuale = 0.50

elif profilo == "Bilanciato (0,75%)":
    rischio_percentuale = 0.75

else:
    rischio_percentuale = 1


# =========================
# ANALISI
# =========================

if st.button("🚀 ANALIZZA"):


    risultato_vwap = analizza_vwap(
        spx,
        vwap
    )


    sopra_vwap = (
        risultato_vwap["posizione"]
        ==
        "Sopra VWAP"
    )


    risultato_score = calcola_score(
        vix,
        trend,
        sopra_vwap,
        evento_macro == "si",
        range_normale == "si",
        gex
    )


    macro = controlla_evento_macro(
        "nessuno"
    )


    strategia = scegli_strategia(
        risultato_score["score"],
        trend,
        sopra_vwap,
        vix,
        range_normale == "si",
        gex
    )


    trade = seleziona_strike(
        spx,
        strategia["strategia"]
    )


    rischio = controlla_rischio(
        capitale,
        rischio_percentuale,
        trade.get(
            "rischio",
            0
        )
    )


    adattamento = adatta_trade(
        trade,
        rischio["rischio_massimo"]
    )


    decisione = genera_decisione(
        risultato_score["score"],
        strategia["strategia"],
        rischio,
        macro,
        adattamento
    )


    # =====================
    # OUTPUT
    # =====================

    st.divider()

    st.subheader("📊 VWAP")
    st.write(risultato_vwap)


    st.subheader("📈 TREND ENGINE v1.7")
    st.write(risultato_trend)


    st.subheader("📈 SCORE")
    st.write(risultato_score)


    st.subheader("🎯 STRATEGIA")
    st.write(strategia)


    st.subheader("💵 TRADE")
    st.write(trade)


    st.subheader("🛡 RISK MANAGER")
    st.write(rischio)


    st.subheader("🔧 ADATTAMENTO")
    st.write(adattamento)


    st.subheader("🚦 DECISIONE FINALE")
    st.write(decisione)
