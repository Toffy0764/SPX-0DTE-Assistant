def controlla_rischio(capitale, rischio_percentuale, rischio_trade, moltiplicatore_size=1):

    """
    Controllo rischio con adattamento evento macro.
    """

    rischio_percentuale_effettivo = (
        rischio_percentuale * moltiplicatore_size
    )

    rischio_massimo = (
        capitale * rischio_percentuale_effettivo / 100
    )

    rapporto_rischio = (
        rischio_trade / rischio_massimo
        if rischio_massimo > 0
        else 0
    )


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
