def verifica_vwap(spx, vwap):

    if spx > vwap:
        return {
            "sopra_vwap": True,
            "segnale": "Sopra VWAP"
        }

    else:
        return {
            "sopra_vwap": False,
            "segnale": "Sotto VWAP"
        }
