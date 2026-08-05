def scegli_strategia(score, trend, sopra_vwap, vix, range_stretto, gex):

    strategia = "NO TRADE"
    motivazione = []

    trend_positivo = [
        "positivo",
        "BULLISH",
        "STRONG BULLISH"
    ]

    trend_negativo = [
        "negativo",
        "BEARISH",
        "STRONG BEARISH"
    ]

    # =========================
    # BULL PUT SPREAD
    # =========================

    if (
        score >= 80
        and trend in trend_positivo
        and sopra_vwap
        and vix < 25
    ):

        strategia = "BULL PUT SPREAD"

        motivazione.append(f"Trend favorevole ({trend})")
        motivazione.append("Prezzo sopra VWAP")
        motivazione.append("Volatilità controllata")

    # =========================
    # BEAR CALL SPREAD
    # =========================

    elif (
        score >= 80
        and trend in trend_negativo
        and not sopra_vwap
        and vix < 25
    ):

        strategia = "BEAR CALL SPREAD"

        motivazione.append(f"Trend favorevole ({trend})")
        motivazione.append("Prezzo sotto VWAP")
        motivazione.append("Volatilità controllata")

    # =========================
    # IRON CONDOR
    # =========================

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

    # =========================
    # NO TRADE
    # =========================

    else:

        motivazione.append("Condizioni non sufficienti")

    return {
        "strategia": strategia,
        "motivazione": motivazione
    }
