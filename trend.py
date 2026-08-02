def calcola_ema(prezzi, periodo):

    if len(prezzi) == 0:
        return 0

    if len(prezzi) < periodo:
        return prezzi[-1]

    moltiplicatore = 2 / (periodo + 1)

    ema = prezzi[0]

    for prezzo in prezzi[1:]:
        ema = (
            prezzo * moltiplicatore
            +
            ema * (1 - moltiplicatore)
        )

    return ema



def analizza_trend(prezzi, vwap):

    motivazioni = []

    score_trend = 0

    prezzo = prezzi[-1]


    # VWAP

    if prezzo > vwap:

        score_trend += 15

        motivazioni.append(
            "Prezzo sopra VWAP"
        )

    elif prezzo < vwap:

        score_trend -= 15

        motivazioni.append(
            "Prezzo sotto VWAP"
        )



    # EMA

    ema20 = calcola_ema(
        prezzi,
        20
    )

    ema50 = calcola_ema(
        prezzi,
        50
    )


    if ema20 > ema50:

        score_trend += 20

        motivazioni.append(
            "EMA20 sopra EMA50"
        )

    elif ema20 < ema50:

        score_trend -= 20

        motivazioni.append(
            "EMA20 sotto EMA50"
        )



    # Momentum

    if len(prezzi) >= 5:

        variazione = prezzo - prezzi[-5]


        if variazione > 0:

            score_trend += 10

            motivazioni.append(
                "Momentum positivo"
            )

        elif variazione < 0:

            score_trend -= 10

            motivazioni.append(
                "Momentum negativo"
            )



    # Trend finale

    if score_trend >= 25:

        trend = "positivo"


    elif score_trend <= -25:

        trend = "negativo"


    else:

        trend = "neutro"



    confidenza = min(
        abs(score_trend) * 3,
        95
    )


    return {

        "trend": trend,

        "score_trend": score_trend,

        "confidenza": confidenza,

        "ema20": round(ema20,2),

        "ema50": round(ema50,2),

        "motivazioni": motivazioni

    }
