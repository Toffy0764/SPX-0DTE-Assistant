import pandas as pd


def calcola_ema(prezzi, periodo):

    serie = pd.Series(prezzi)

    return (
        serie
        .ewm(
            span=periodo,
            adjust=False
        )
        .mean()
    )



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


    prezzo = float(
        serie.iloc[-1]
    )


    ema20 = calcola_ema(
        prezzi,
        20
    )

    ema50 = calcola_ema(
        prezzi,
        50
    )


    valore_ema20 = float(
        ema20.iloc[-1]
    )

    valore_ema50 = float(
        ema50.iloc[-1]
    )


    slope_ema20 = (
        valore_ema20
        -
        float(ema20.iloc[-5])
    )


    slope_ema50 = (
        valore_ema50
        -
        float(ema50.iloc[-5])
    )


    momentum = (
        prezzo
        -
        float(serie.iloc[-10])
    )


    # =====================
    # VWAP DISTANCE
    # =====================

    distanza_vwap = (
        prezzo - vwap
    )


    distanza_percentuale = (
        distanza_vwap / vwap
    ) * 100



    punteggio = 0

    motivazioni = []



    # Prezzo vs VWAP

    if prezzo > vwap:

        punteggio += 20

        motivazioni.append(
            "Prezzo sopra VWAP"
        )

    else:

        punteggio -= 20

        motivazioni.append(
            "Prezzo sotto VWAP"
        )



    # EMA structure

    if valore_ema20 > valore_ema50:

        punteggio += 25

        motivazioni.append(
            "EMA20 sopra EMA50"
        )

    else:

        punteggio -= 25

        motivazioni.append(
            "EMA20 sotto EMA50"
        )



    # EMA slope

    if slope_ema20 > 0:

        punteggio += 15

        motivazioni.append(
            "EMA20 crescente"
        )



    if slope_ema50 > 0:

        punteggio += 10

        motivazioni.append(
            "EMA50 crescente"
        )



    # Momentum

    if momentum > 0:

        punteggio += 15

        motivazioni.append(
            "Momentum positivo"
        )

    else:

        punteggio -= 10

        motivazioni.append(
            "Momentum negativo"
        )



    # =====================
    # ESTENSIONE VWAP
    # =====================

    if abs(distanza_percentuale) > 0.60:

        punteggio -= 20

        stato_estensione = "ECCESSIVA"

        motivazioni.append(
            "Prezzo molto distante dal VWAP"
        )


    elif abs(distanza_percentuale) > 0.30:

        punteggio -= 5

        stato_estensione = "MODERATA"

        motivazioni.append(
            "Prezzo leggermente esteso dal VWAP"
        )


    else:

        stato_estensione = "NORMALE"

        motivazioni.append(
            "Distanza VWAP normale"
        )



    forza = max(
        min(
            punteggio,
            100
        ),
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



    return {


        "trend": trend,


        "forza_trend": forza,


        "confidenza": forza,


        "prezzo": round(
            prezzo,
            2
        ),


        "vwap": round(
            float(vwap),
            2
        ),


        "distanza_vwap_punti": round(
            distanza_vwap,
            2
        ),


        "distanza_vwap_percentuale": round(
            distanza_percentuale,
            3
        ),


        "ema20": round(
            valore_ema20,
            2
        ),


        "ema50": round(
            valore_ema50,
            2
        ),


        "pendenza_ema20": round(
            slope_ema20,
            2
        ),


        "pendenza_ema50": round(
            slope_ema50,
            2
        ),


        "momentum_10_barre": round(
            momentum,
            2
        ),


        "stato_estensione": stato_estensione,


        "motivazioni": motivazioni

    }
