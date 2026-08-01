def genera_decisione(score, strategia, rischio, macro, trade_adattato=None):
    """
    Genera la decisione finale considerando:
    - qualità del setup
    - rischio originale
    - eventuale adattamento del trade
    """

    motivi = []


    # Caso 1: rischio originale accettabile

    if rischio["stato"] == "APPROVATO":

        return {
            "decisione": "OPERARE",
            "motivi": [
                "Rischio compatibile con il capitale",
                "Trade approvato dal Risk Manager"
            ]
        }


    # Caso 2: rischio bloccato ma trade adattato

    if (
        trade_adattato
        and trade_adattato.get("stato") == "ADATTATO"
        and trade_adattato.get("rischio_stimato", 999999)
        <= rischio["rischio_massimo"]
    ):

        return {
            "decisione": "OPERARE CON ADATTAMENTO",
            "motivi": [
                "Setup di mercato favorevole",
                "Rischio iniziale troppo elevato",
                "Trade modificato entro il limite consentito"
            ]
        }


    # Caso 3: nessuna soluzione

    return {
        "decisione": "NON OPERARE",
        "motivi": [
            "Rischio non compatibile con il capitale"
        ]
    }
