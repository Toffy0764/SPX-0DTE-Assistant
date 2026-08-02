import yfinance as yf
import pandas as pd


TICKER = "^GSPC"


def get_data():

    dati = yf.download(
        TICKER,
        period="5d",
        interval="15m",
        progress=False,
        auto_adjust=False
    )

    if dati.empty:
        raise Exception(
            "Nessun dato ricevuto da Yahoo Finance"
        )

    return dati



def get_spx_price():

    dati = get_data()

    ultimo = dati["Close"].iloc[-1]

    if isinstance(ultimo, pd.Series):
        ultimo = ultimo.iloc[0]

    return round(
        float(ultimo),
        2
    )



def get_intraday_prices():

    dati = get_data()

    prezzi = dati["Close"]

    if isinstance(prezzi, pd.DataFrame):
        prezzi = prezzi.iloc[:,0]


    prezzi = (
        prezzi
        .dropna()
        .tolist()
    )


    if len(prezzi) == 0:
        raise Exception(
            "Serie prezzi vuota"
        )


    return [
        round(float(x),2)
        for x in prezzi
    ]



def get_vwap():

    dati = get_data()


    close = dati["Close"]
    volume = dati["Volume"]


    if isinstance(close, pd.DataFrame):
        close = close.iloc[:,0]

    if isinstance(volume, pd.DataFrame):
        volume = volume.iloc[:,0]


    vwap = (
        (close * volume).sum()
        /
        volume.sum()
    )


    return round(
        float(vwap),
        2
    )
