def controlla_rischio(capitale, rischio_percentuale, rischio_trade):
    """
    Controlla se il rischio della posizione è compatibile
    con il capitale disponibile.
    """

    rischio_massimo = capitale * rischio_percentuale / 100

    if rischio_trade <= rischio_massimo:
        stato = "APPROVATO"
        contratti = int(rischio_massimo // rischio_trade)
        if contratti < 1:
            contratti = 1
    else:
        stato = "BLOCCATO"
        contratti = 0

    return {
        "rischio_massimo": rischio_massimo,
        "rischio_trade": rischio_trade,
        "stato": stato,
        "contratti": contratti
    }
