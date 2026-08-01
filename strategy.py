def scegli_strategia(score, trend, sopra_vwap, vix, range_stretto, gex):
    strategia = "NO TRADE"
    motivazione = []

    # Bull Put Spread
    if (
        score >= 80
        and trend == "positivo"
        and sopra_vwap
        and vix < 25
    ):
        strategia = "BULL PUT SPREAD"
        motivazione.append("Trend positivo")
        motivazione.append("Prezzo sopra VWAP")
        motivazione.append("Volatilita controllata")

    # Bear Call Spread
    elif (
        score >= 80
        and trend == "negativo"
        and not sopra_vwap
        and vix < 25
    ):
        strategia = "BEAR CALL SPREAD"
        motivazione.append("Trend negativo")
        motivazione.append("Prezzo sotto VWAP")
        motivazione.append("Volatilita controllata")

    # Iron Condor
    elif (
        score >= 85
        and range_stretto
        and vix < 20
        and gex == "positivo"
    ):
        strategia = "IRON CONDOR"
        motivazione.append("Mercato laterale")
        motivazione.append("Range contenuto")
        motivazione.append("Gamma favorevole")

    else:
        motivazione.append("Condizioni non sufficienti")

    return {
        "strategia": strategia,
        "motivazione": motivazione
    }
