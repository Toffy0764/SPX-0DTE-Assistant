import streamlit as st

from score import calcola_score
from strategy import scegli_strategia
from risk_manager import controlla_rischio
from strikes import seleziona_strike
from vwap import analizza_vwap
from macro import controlla_evento_macro
from decision import genera_decisione
from adjustment import adatta_trade


st.set_page_config(
    page_title="SPX 0DTE Assistant",
    layout="centered"
)


st.title("SPX 0DTE Assistant")
st.write("Professional Decision Engine v1.2")


# =========================
# INPUT
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

trend = st.selectbox(
    "Trend",
    ["positivo", "neutro", "negativo"]
)

evento_macro = st.selectbox(
    "Evento macro importante",
    ["no", "si"]
)

evento_macro_livello = st.selectbox(
    "Rischio evento macro",
    ["nessuno", "medio", "alto"]
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


# =========================
# ANALISI
# =========================

if st.button("🚀 ANALIZZA GIORNATA"):


    risultato_vwap = analizza_vwap(
        spx,
        vwap
    )


    sopra_vwap = (
        risultato_vwap["posizione"] == "Sopra VWAP"
    )


    analisi_macro = controlla_evento_macro(
        evento_macro_livello
    )


    risultato_score = calcola_score(
        vix,
        trend,
        sopra_vwap,
        evento_macro == "si",
        range_normale == "si",
        gex
    )


    risultato_strategia = scegli_strategia(
        risultato_score["score"],
        trend,
        sopra_vwap,
        vix,
        range_normale == "si",
        gex
    )


    risultato_strike = seleziona_strike(
        spx,
        risultato_strategia["strategia"]
    )


    rischio = controlla_rischio(
        capitale,
        0.5,
        risultato_strike.get("rischio", 0),
        analisi_macro["moltiplicatore_size"]
    )


    trade_adattato = adatta_trade(
        risultato_strike,
        rischio["rischio_massimo"]
    )


    decisione_finale = genera_decisione(
        risultato_score["score"],
        risultato_strategia["strategia"],
        rischio,
        analisi_macro
    )


    # =========================
    # DASHBOARD
    # =========================

    st.divider()

    st.subheader("📈 MARKET STATUS")


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "SCORE",
            f'{risultato_score["score"]}/100'
        )


    with col2:

        st.metric(
            "STATO",
            risultato_score["stato"]
        )


    if risultato_score["stato"] == "VERDE":

        st.success(
            "🟢 MERCATO FAVOREVOLE"
        )

    elif risultato_score["stato"] == "GIALLO":

        st.warning(
            "🟡 ATTENZIONE"
        )

    else:

        st.error(
            "🔴 NON OPERARE"
        )


    st.divider()


    st.subheader("📊 ANALISI VWAP")

    st.write(
        risultato_vwap
    )


    st.subheader("🌍 EVENTO MACRO")

    st.write(
        analisi_macro
    )


    st.subheader("🎯 STRATEGIA")

    st.write(
        risultato_strategia["strategia"]
    )

    st.write(
        risultato_strategia["motivazione"]
    )


    st.subheader("💵 TRADE PROPOSTO")

    st.write(
        risultato_strike
    )


    st.subheader("🛡 RISK MANAGER")

    st.write(
        rischio
    )


    st.subheader("🔧 TRADE ADJUSTMENT")

    st.write(
        trade_adattato
    )


    st.divider()


    st.subheader("🚦 DECISIONE FINALE")


    if decisione_finale["decisione"] == "NON OPERARE":

        st.error(
            "❌ NON OPERARE"
        )

    else:

        st.success(
            decisione_finale["decisione"]
        )


    st.write(
        decisione_finale["motivi"]
    )
