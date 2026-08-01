def seleziona_strike(spx, strategia):

    risultato = {}

    if strategia == "BULL PUT SPREAD":

        short_strike = round(spx - 40, -1)
        long_strike = short_strike - 10

        risultato = {
            "strategia": strategia,
            "vendita": f"PUT {short_strike}",
            "acquisto": f"PUT {long_strike}",
            "credito_stimato": 1.20,
            "rischio": 880
        }

    elif strategia == "BEAR CALL SPREAD":

        short_strike = round(spx + 40, -1)
        long_strike = short_strike + 10

        risultato = {
            "strategia": strategia,
            "vendita": f"CALL {short_strike}",
            "acquisto": f"CALL {long_strike}",
            "credito_stimato": 1.20,
            "rischio": 880
        }

    elif strategia == "IRON CONDOR":

        risultato = {
            "strategia": strategia,
            "nota": "Configurazione iron condor da definire"
        }

    else:

        risultato = {
            "strategia": "NO TRADE",
            "nota": "Nessuna operazione proposta"
        }

    return risultato
