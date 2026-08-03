def controlla_rischio(
    capitale,
    rischio_percentuale,
    rischio_trade,
    moltiplicatore_size=1
):
    """
    Controllo rischio con protezione da valori non validi.
    """

    rischio_percentuale_effettivo = (
        rischio_percentuale * moltiplicatore_size
    )

    rischio_massimo = (
        capitale * rischio_percentuale_effettivo / 100
    )

    # Protezione
    if rischio_trade <= 0:

        return {
            "rischio_massimo": round(rischio_massimo, 2),
            "rischio_trade": rischio_trade,
            "rapporto_rischio": 0,
            "stato": "ERRORE",
            "contratti": 0,
            "motivo": "Rischio trade non valido",
            "moltiplicatore_size": moltiplicatore_size
        }

    rapporto_rischio = (
        rischio_trade / rischio_massimo
        if rischio_massimo > 0
        else 0
    )

    if rischio_trade <= rischio_massimo:

        stato = "APPROVATO"

        contratti = max(
            1,
            int(rischio_massimo // rischio_trade)
        )

        motivo = "Rischio compatibile con capitale"

    else:

        stato = "BLOCCATO"

        contratti = 0

        motivo = (
            "Rischio superiore al limite "
            "considerando il contesto macro"
        )

    return {
        "rischio_massimo": round(rischio_massimo, 2),
        "rischio_trade": rischio_trade,
        "rapporto_rischio": round(rapporto_rischio, 2),
        "stato": stato,
        "contratti": contratti,
        "motivo": motivo,
        "moltiplicatore_size": moltiplicatore_size
    }
