def seleziona_strike(spx, strategia):

    if strategia == "BULL PUT SPREAD":

        short_strike = round(spx - 40, -1)
        long_strike = short_strike - 10

        return {
            "strategia": strategia,
            "vendita": f"PUT {short_strike}",
            "acquisto": f"PUT {long_strike}",
            "credito_stimato": 1.20,
            "rischio": 880,
            "valido": True
        }

    elif strategia == "BEAR CALL SPREAD":

        short_strike = round(spx + 40, -1)
        long_strike = short_strike + 10

        return {
            "strategia": strategia,
            "vendita": f"CALL {short_strike}",
            "acquisto": f"CALL {long_strike}",
            "credito_stimato": 1.20,
            "rischio": 880,
            "valido": True
        }

    elif strategia == "IRON CONDOR":

        return {
            "strategia": strategia,
            "vendita": "",
            "acquisto": "",
            "credito_stimato": 0,
            "rischio": 0,
            "nota": "Configurazione Iron Condor non ancora implementata",
            "valido": False
        }

    else:

        return {
            "strategia": "NO TRADE",
            "vendita": "",
            "acquisto": "",
            "credito_stimato": 0,
            "rischio": 0,
            "nota": "Nessuna operazione proposta",
            "valido": False
        }
