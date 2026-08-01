def adatta_trade(trade, rischio_massimo):
    """
    Cerca di adattare il trade quando il rischio
    supera il limite consentito.
    """

    risultato = {}

    rischio_attuale = trade.get("rischio", 0)

    if rischio_attuale <= rischio_massimo:

        return {
            "stato": "OK",
            "messaggio": "Trade già compatibile con il rischio",
            "trade": trade
        }


    # Riduzione spread
    if trade.get("strategia") == "BULL PUT SPREAD":

        risultato = {
            "stato": "ADATTATO",
            "strategia": "BULL PUT SPREAD",
            "vendita": trade["vendita"],
            "acquisto": "Ridotto spread",
            "rischio_stimato": round(rischio_attuale / 2, 0),
            "messaggio": "Riduzione rischio tramite spread più stretto"
        }


    elif trade.get("strategia") == "BEAR CALL SPREAD":

        risultato = {
            "stato": "ADATTATO",
            "strategia": "BEAR CALL SPREAD",
            "vendita": trade["vendita"],
            "acquisto": "Ridotto spread",
            "rischio_stimato": round(rischio_attuale / 2, 0),
            "messaggio": "Riduzione rischio tramite spread più stretto"
        }


    else:

        risultato = {
            "stato": "NON POSSIBILE",
            "messaggio": "Nessun adattamento disponibile"
        }


    return risultato
