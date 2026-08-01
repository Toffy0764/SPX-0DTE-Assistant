def controlla_rischio(capitale, rischio_percentuale, rischio_trade):

    """
    Controllo rischio per strategie con opzioni.
    """

    rischio_massimo = capitale * rischio_percentuale / 100

    rapporto_rischio = rischio_trade / rischio_massimo if rischio_massimo > 0 else 0

    if rischio_trade <= rischio_massimo:

        stato = "APPROVATO"

        contratti = int(
            rischio_massimo // rischio_trade
        )

        if contratti < 1:
            contratti = 1

        motivo = "Rischio compatibile con capitale"

    else:

        stato = "BLOCCATO"

        contratti = 0

        motivo = "Rischio minimo della strategia superiore al limite consentito"


    return {
        "rischio_massimo": round(rischio_massimo, 2),
        "rischio_trade": rischio_trade,
        "rapporto_rischio": round(rapporto_rischio, 2),
        "stato": stato,
        "contratti": contratti,
        "motivo": motivo
    }
