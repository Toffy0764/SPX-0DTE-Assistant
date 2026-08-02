from datetime import datetime
import pytz


def market_status():

    """
    Controlla se il mercato USA è aperto.
    Orario NYSE:
    09:30 - 16:00 New York
    """

    tz = pytz.timezone(
        "America/New_York"
    )

    ora_ny = datetime.now(tz)

    giorno = ora_ny.weekday()

    minuti = (
        ora_ny.hour * 60
        +
        ora_ny.minute
    )


    apertura = 9 * 60 + 30

    chiusura = 16 * 60



    # Sabato e domenica

    if giorno >= 5:

        return {

            "stato": "CHIUSO",

            "motivo": "Weekend",

            "operativita": False

        }



    # Fuori orario

    if minuti < apertura or minuti >= chiusura:

        return {

            "stato": "CHIUSO",

            "motivo": "Fuori orario mercato USA",

            "operativita": False

        }



    return {

        "stato": "APERTO",

        "motivo": "Sessione regolare USA",

        "operativita": True

    }
