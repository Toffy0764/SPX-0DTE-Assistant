import csv
import os
from datetime import datetime


FILE_JOURNAL = "trade_journal.csv"


def salva_analisi(dati):

    file_esiste = os.path.isfile(FILE_JOURNAL)

    with open(
        FILE_JOURNAL,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=dati.keys()
        )

        if not file_esiste:
            writer.writeheader()

        writer.writerow(dati)



def crea_record_base(
    spx,
    vix,
    vwap,
    trend,
    score,
    strategia,
    trade,
    rischio,
    decisione,
    risultato_trend
):

    return {

        "data_ora":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "SPX":
            spx,

        "VIX":
            vix,

        "VWAP":
            vwap,

        "trend":
            trend,

        "forza_trend":
            risultato_trend.get(
                "forza_trend",
                ""
            ),

        "distanza_vwap_percentuale":
            risultato_trend.get(
                "distanza_vwap_percentuale",
                ""
            ),

        "score":
            score.get(
                "score",
                ""
            ),

        "strategia":
            strategia.get(
                "strategia",
                ""
            ),

        "trade":
            str(trade),

        "rischio":
            str(rischio),

        "decisione":
            str(decisione),

        "esito":
            "",

        "pnl":
            "",

        "note":
            ""
    }
