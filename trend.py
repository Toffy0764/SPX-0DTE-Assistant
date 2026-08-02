import pandas as pd


def calcola_ema(prezzi, periodo):

    serie = pd.Series(prezzi)

    ema = (
        serie
        .ewm(
            span=periodo,
            adjust=False
        )
        .mean()
    )

    return ema



def analizza_trend(prezzi, vwap):

    if len(prezzi) < 50:

        return {

            "trend": "NEUTRO",

            "forza_trend": 0,

            "confidenza": 0,

            "motivazioni": [
                "Dati insufficienti"
            ]

        }



    serie = pd.Series(prezzi)


    ema20 = calcola_ema(
        prezzi,
        20
    )


    ema50 = calcola_ema(
        prezzi,
        50
    )


    prezzo_attuale = (
        serie.iloc[-1]
    )


    valore_ema20 = (
        ema20.iloc[-1]
    )


    valore_ema50 = (
        ema50.iloc[-1]
    )


    # Pendenza EMA

    slope_ema20 = (
        valore_ema20
        -
        ema20.iloc[-5]
    )


    slope_ema50 = (
        valore_ema50
        -
        ema50.iloc[-5]
    )



    # Momentum ultime 10 barre

    momentum = (
        serie.iloc[-1]
        -
        serie.iloc[-10]
    )



    punteggio = 0

    motivazioni = []



    # Prezzo rispetto al VWAP

    if prezzo_attuale > vwap:

        punteggio += 25

        motivazioni.append(
            "Prezzo sopra VWAP"
        )

    else:

        punteggio -= 15

        motivazioni.append(
            "Prezzo sotto VWAP"
        )



    # EMA20 vs EMA50

    if valore_ema20 > valore_ema50:

        punteggio += 35

        motivazioni.append(
            "EMA20 sopra EMA50"
        )

    else:

        punteggio -= 25

        motivazioni.append(
            "EMA20 sotto EMA50"
        )



    # Pendenza EMA20

    if slope_ema20 > 0:

        punteggio += 15

        motivazioni.append(
            "EMA20 crescente"
        )

    else:

        motivazioni.append(
            "EMA20 in calo"
        )



    # Momentum

    if momentum > 0:

        punteggio += 25

        motivazioni.append(
            "Momentum positivo"
        )

    else:

        punteggio -= 10

        motivazioni.append(
            "Momentum negativo"
        )



    forza = max(
        min(punteggio,100),
        0
    )



    if forza >= 80:

        trend = "STRONG BULLISH"

    elif forza >= 60:

        trend = "BULLISH"

    elif forza >= 40:

        trend = "NEUTRO"

    else:

        trend = "BEARISH"



    confidenza = forza



    return {

        "trend": trend,

        "forza_trend": forza,

        "confidenza": confidenza,

        "prezzo": round(
            float(prezzo_attuale),
            2
        ),

        "vwap": round(
            float(vwap),
            2
        ),

        "ema20": round(
            float(valore_ema20),
            2
        ),

        "ema50": round(
            float(valore_ema50),
            2
        ),

        "pendenza_ema20": round(
            float(slope_ema20),
            2
        ),

        "pendenza_ema50": round(
            float(slope_ema50),
            2
        ),

        "momentum_10_barre": round(
            float(momentum),
            2
        ),

        "motivazioni": motivazioni

    }
