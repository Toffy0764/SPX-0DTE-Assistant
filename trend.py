def analizza_trend(prezzo, vwap):
    """
    Trend Engine v1.6

    Analizza:
    - posizione rispetto al VWAP
    - distanza dal VWAP
    - forza del movimento

    Output:
    trend
    score
    confidenza
    motivazioni
    """

    motivazioni = []

    score_trend = 0


    # Distanza dal VWAP

    distanza = prezzo - vwap


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

    else:

        motivazioni.append(
            "Prezzo sul VWAP"
        )


    # Forza distanza dal VWAP

    distanza_percentuale = (
        abs(distanza) / vwap
    ) * 100


    if distanza_percentuale >= 0.30:

        if prezzo > vwap:

            score_trend += 10

            motivazioni.append(
                "Distanza dal VWAP favorevole"
            )

        else:

            score_trend -= 10

            motivazioni.append(
                "Distanza dal VWAP negativa"
            )


    # Classificazione trend

    if score_trend >= 20:

        trend = "positivo"


    elif score_trend <= -20:

        trend = "negativo"


    else:

        trend = "neutro"



    # Confidenza

    confidenza = min(
        abs(score_trend) * 4,
        95
    )


    return {

        "trend": trend,

        "score_trend": score_trend,

        "confidenza": confidenza,

        "distanza_vwap_percentuale":
            round(
                distanza_percentuale,
                2
            ),

        "motivazioni": motivazioni

    }
