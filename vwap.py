def analizza_vwap(spx, vwap):

    distanza_punti = spx - vwap
    distanza_percentuale = (distanza_punti / vwap) * 100

    if spx > vwap:
        posizione = "Sopra VWAP"
    else:
        posizione = "Sotto VWAP"

    if 0 <= distanza_percentuale <= 0.5:
        segnale = "Zona favorevole"
    elif distanza_percentuale > 0.5:
        segnale = "Possibile estensione"
    else:
        segnale = "Debolezza"

    return {
        "posizione": posizione,
        "distanza_punti": round(distanza_punti, 1),
        "distanza_percentuale": round(distanza_percentuale, 2),
        "segnale": segnale
    }
