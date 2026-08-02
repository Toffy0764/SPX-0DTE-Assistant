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

    return round(
        float(ema.iloc[-1]),
        2
    )



def analizza_trend(prezzi, vwap):

    if len(prezzi) < 50:

        return {

            "trend": "NEUTRO",

            "forza": 0,

            "motivazioni": [
                "Dati insufficienti"
            ]

        }



    ema20 = calcola_ema(
        prezzi,
        20
    )


    ema50 = calcola_ema(
        prezzi,
        50
    )


    prezzo_attuale = prezzi[-1]


    momentum = (

        prezzi[-1]
        -
        prezzi[-10]

    )


    motivazioni = []

    punteggio = 0



    # VWAP

    if prezzo_attuale > vwap:

        punteggio += 30

        motivazioni.append(
            "Prezzo sopra VWAP"
        )

    else:

        punteggio -= 20

        motivazioni.append(
            "Prezzo sotto VWAP"
        )



    # EMA

    if ema20 > ema50:

        punteggio += 40

        motivazioni.append(
            "EMA20 sopra EMA50"
        )

    else:

        punteggio -= 30

        motivazioni.append(
            "EMA20 sotto EMA50"
        )



    # Momentum

    if momentum > 0:

        punteggio += 30

        motivazioni.append(
            "Momentum positivo"
        )

    else:

        punteggio -= 20

        motivazioni.append(
            "Momentum negativo"
        )



    if punteggio >= 60:

        trend = "POSITIVO"


    elif punteggio <= 30:

        trend = "NEGATIVO"


    else:

        trend = "NEUTRO"



    return {

        "trend": trend,

        "forza": min(
            max(punteggio,0),
            100
        ),

        "prezzo": prezzo_attuale,

        "VWAP": vwap,

        "EMA20": ema20,

        "EMA50": ema50,

        "momentum_10_barre": round(
            float(momentum),
            2
        ),

        "motivazioni": motivazioni

    }
