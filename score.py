def calcola_score(vix, trend, sopra_vwap, evento_macro, range_normale, gex):

    score = 0
    motivi = []

    # =========================
    # VIX
    # =========================

    if vix < 20:
        score += 20
        motivi.append("VIX favorevole")

    elif vix < 25:
        score += 10
        motivi.append("VIX neutro")

    else:
        motivi.append("VIX elevato")


    # =========================
    # TREND E VWAP
    # =========================

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


    if trend in trend_positivo and sopra_vwap:

        score += 25
        motivi.append(
            f"Trend favorevole ({trend}) sopra VWAP"
        )


    elif trend == "neutro":

        score += 12
        motivi.append(
            "Trend neutro"
        )


    else:

        motivi.append(
            f"Trend non favorevole ({trend})"
        )


    # =========================
    # EVENTO MACRO
    # =========================

    if not evento_macro:

        score += 15
        motivi.append(
            "Nessun evento macro importante"
        )

    else:

        motivi.append(
            "Evento macro presente"
        )


    # =========================
    # RANGE
    # =========================

    if range_normale:

        score += 20
        motivi.append(
            "Range normale"
        )


    # =========================
    # GEX
    # =========================

    if gex == "positivo":

        score += 20
        motivi.append(
            "Gamma favorevole"
        )


    elif gex == "neutro":

        score += 10
        motivi.append(
            "Gamma neutrale"
        )


    # =========================
    # SEMAFORO
    # =========================

    if score >= 80:

        stato = "VERDE"

    elif score >= 65:

        stato = "GIALLO"

    else:

        stato = "ROSSO"


    return {

        "score": score,

        "stato": stato,

        "motivi": motivi,

        "dettaglio": {
            "fattori": motivi
        }

    }
