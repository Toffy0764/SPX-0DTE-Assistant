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

st.write(
    "Analisi giornaliera mercato e gestione rischio"
)


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
    min_value=0.0,
    value=18.0
)


evento_macro = st.selectbox(
    "Evento macro importante",
    [
        "no",
        "si"
    ]
)


range_normale = st.selectbox(
    "Range normale",
    [
        "si",
        "no"
    ]
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
# TREND AUTOMATICO
# =========================

risultato_trend = analizza_trend(
    spx,
    vwap
)

trend = risultato_trend["trend"]


# =========================
# GESTIONE RISCHIO
# =========================

st.subheader("🛡 Gestione rischio")


capitale = st.number_input(
    "Capitale disponibile",
    value=100000
)


profilo_rischio = st.selectbox(
    "Profilo di rischio",
    [
        "Conservativo (0,25%)",
        "Moderato (0,50%)",
        "Bilanciato (0,75%)",
        "Dinamico (1,00%)",
        "Personalizzato"
    ]
)


if profilo_rischio == "Conservativo (0,25%)":

    rischio_percentuale = 0.25

elif profilo_rischio == "Moderato (0,50%)":

    rischio_percentuale = 0.50

elif profilo_rischio == "Bilanciato (0,75%)":

    rischio_percentuale = 0.75

elif profilo_rischio == "Dinamico (1,00%)":

    rischio_percentuale = 1.00

else:

    rischio_percentuale = st.number_input(
        "Rischio personalizzato (%)",
        min_value=0.10,
        max_value=5.00,
        value=0.50,
        step=0.05
    )


rischio_massimo_euro = (
    capitale *
    rischio_percentuale /
    100
)


st.info(
    f"Rischio massimo per trade: {rischio_massimo_euro:.0f} €"
)


evento_macro_livello = st.selectbox(
    "Rischio evento macro",
    [
        "nessuno",
        "medio",
        "alto"
    ]
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


    analisi_macro = controlla_evento_macro(
        evento_macro_livello
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
        rischio_percentuale,
        risultato_strike.get(
            "rischio",
            0
        )
    )


    trade_adattato = adatta_trade(
        risultato_strike,
        rischio["rischio_massimo"]
    )


    decisione_finale = genera_decisione(
        risultato_score["score"],
        risultato_strategia["strategia"],
        rischio,
        analisi_macro,
        trade_adattato
    )


    # =========================
    # RISULTATI
    # =========================

    st.divider()


    st.subheader("📊 ANALISI VWAP")
    st.write(
        risultato_vwap
    )


    st.subheader("📈 TREND AUTOMATICO")
    st.write(
        risultato_trend
    )


    st.subheader("🌍 EVENTO MACRO")
    st.write(
        analisi_macro
    )


    st.subheader("📈 RISULTATO")

    st.write(
        f"Score: {risultato_score['score']} /100"
    )

    st.write(
        f"Stato: {risultato_score['stato']}"
    )


    st.subheader("Motivazioni")

    st.write(
        risultato_score["motivi"]
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


    st.subheader("🚦 DECISIONE FINALE")

    st.write(
        decisione_finale
    )
