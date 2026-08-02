import yfinance as yf
import pandas as pd


TICKER = "^GSPC"


def get_data():

    dati = yf.download(
        TICKER,
        period="1d",
        interval="5m",
        progress=False,
        auto_adjust=False
    )

    if dati.empty:
        raise Exception(
            "Nessun dato ricevuto da Yahoo Finance"
        )

    return dati



def normalizza_colonna(colonna):

    """
    Yahoo può restituire colonne
    con struttura multipla.
    """

    if isinstance(colonna, pd.DataFrame):

        return colonna.iloc[:, 0]

    return colonna



def get_spx_price():

    dati = get_data()

    close = normalizza_colonna(
        dati["Close"]
    )

    ultimo = (
        close
        .dropna()
        .iloc[-1]
    )

    return round(
        float(ultimo),
        2
    )



def get_intraday_prices():

    dati = get_data()

    close = normalizza_colonna(
        dati["Close"]
    )

    prezzi = (
        close
        .dropna()
        .tolist()
    )

    return [
        round(float(x), 2)
        for x in prezzi
    ]



def get_vwap():

    dati = get_data()


    close = normalizza_colonna(
        dati["Close"]
    )

    volume = normalizza_colonna(
        dati["Volume"]
    )


    dati_puliti = pd.DataFrame({

        "close": close,

        "volume": volume

    }).dropna()



    if dati_puliti.empty:

        return round(
            float(close.iloc[-1]),
            2
        )


    volume_totale = (
        dati_puliti["volume"]
        .sum()
    )


    if volume_totale == 0:

        return round(
            float(close.iloc[-1]),
            2
        )


    vwap = (

        dati_puliti["close"]
        *
        dati_puliti["volume"]

    ).sum() / volume_totale


    return round(
        float(vwap),
        2
    )
