def adatta_trade(trade, rischio_massimo):
    """
    Adatta il trade riducendo l'ampiezza dello spread
    quando il rischio supera il limite.
    """

    rischio_attuale = trade.get("rischio", 0)

    if rischio_attuale <= rischio_massimo:

        return {
            "stato": "OK",
            "messaggio": "Trade già compatibile",
            "trade": trade
        }


    strategia = trade.get("strategia")


    if strategia == "BULL PUT SPREAD":

        vendita = trade.get("vendita", "")

        try:
            strike = int(
                vendita.replace("PUT ", "")
            )

            nuovo_acquisto = strike - 5

        except:

            nuovo_acquisto = "da definire"


        return {

            "stato": "ADATTATO",
            "strategia": strategia,
            "vendita": vendita,
            "acquisto": f"PUT {nuovo_acquisto}",
            "rischio_stimato": round(
                rischio_attuale / 2,
                0
            ),
            "messaggio":
            "Spread ridotto da 10 a 5 punti"

        }


    if strategia == "BEAR CALL SPREAD":

        vendita = trade.get("vendita", "")

        try:

            strike = int(
                vendita.replace("CALL ", "")
            )

            nuovo_acquisto = strike + 5

        except:

            nuovo_acquisto = "da definire"


        return {

            "stato": "ADATTATO",
            "strategia": strategia,
            "vendita": vendita,
            "acquisto": f"CALL {nuovo_acquisto}",
            "rischio_stimato": round(
                rischio_attuale / 2,
                0
            ),
            "messaggio":
            "Spread ridotto da 10 a 5 punti"

        }


    return {

        "stato": "NON POSSIBILE",
        "messaggio":
        "Nessun adattamento disponibile"

    }
