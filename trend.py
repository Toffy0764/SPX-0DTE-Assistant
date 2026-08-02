def analizza_trend(prezzo, vwap):
    """
    Analizza il trend di breve periodo
    basandosi sulla posizione del prezzo
    rispetto al VWAP.

    Output:
    - trend
    - punteggio
    - confidenza
    - motivazioni
    """

    motivazioni = []


    score_trend = 0


    # Prezzo sopra/sotto VWAP

    if prezzo > vwap:

        trend = "positivo"

        score_trend += 15

        motivazioni.append(
            "Prezzo sopra VWAP"
        )


    elif prezzo < vwap:

        trend = "negativo"

        score_trend -= 15

        motivazioni.append(
            "Prezzo sotto VWAP"
        )


    else:

        trend = "neutro"

        motivazioni.append(
            "Prezzo sul VWAP"
        )


    # Confidenza

    if score_trend >= 15:

        confidenza = 70


    elif score_trend <= -15:

        confidenza = 70


    else:

        confidenza = 50



    return {

        "trend": trend,

        "score_trend": score_trend,

        "confidenza": confidenza,

        "motivazioni": motivazioni

    }
