def calcola_score(vix, trend, sopra_vwap, evento_macro, range_normale, gex):
    score = 0
    motivi = []

    # 1) VIX - massimo 20 punti
    if vix < 20:
        score += 20
        motivi.append("VIX favorevole")
    elif vix < 25:
        score += 10
        motivi.append("VIX neutro")
    else:
        motivi.append("VIX elevato")

    # 2) Trend e VWAP - massimo 25 punti
    if trend == "positivo" and sopra_vwap:
        score += 25
        motivi.append("Trend positivo sopra VWAP")
    elif trend == "neutro":
        score += 12
        motivi.append("Trend neutro")
    else:
        motivi.append("Trend non favorevole")

    # 3) Eventi macro - massimo 15 punti
    if not evento_macro:
        score += 15
        motivi.append("Nessun evento macro importante")
    else:
        motivi.append("Evento macro presente")

    # 4) Range - massimo 20 punti
    if range_normale:
        score += 20
        motivi.append("Range normale")

    # 5) GEX - massimo 20 punti
    if gex == "positivo":
        score += 20
        motivi.append("Gamma favorevole")
    elif gex == "neutro":
        score += 10
        motivi.append("Gamma neutrale")

    # Semaforo
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
 
