def genera_decisione(score, strategia, rischio, macro):

    decisione = ""
    motivi = []


    if rischio["stato"] == "BLOCCATO":

        decisione = "NON OPERARE"

        motivi.append(
            "Rischio non compatibile con il capitale"
        )


    elif macro["stato"] == "ATTENZIONE":

        decisione = "OPERARE CON CAUTELA"

        motivi.append(
            "Presenza di rischio macro"
        )


    elif score >= 80 and strategia != "NO TRADE":

        decisione = "SETUP OPERABILE"

        motivi.append(
            "Condizioni tecniche favorevoli"
        )


    else:

        decisione = "ATTENDERE"

        motivi.append(
            "Condizioni insufficienti"
        )


    return {
        "decisione": decisione,
        "motivi": motivi
    }
