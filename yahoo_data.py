import yfinance as yf


def get_spx_price():

    ticker = yf.Ticker("^GSPC")

    dati = ticker.history(
        period="1d",
        interval="5m"
    )

    ultimo = dati["Close"].iloc[-1]

    return round(
        float(ultimo),
        2
    )



def get_intraday_prices():

    ticker = yf.Ticker("^GSPC")

    dati = ticker.history(
        period="1d",
        interval="5m"
    )


    prezzi = (
        dati["Close"]
        .dropna()
        .tolist()
    )


    return prezzi



def get_vwap():

    ticker = yf.Ticker("^GSPC")


    dati = ticker.history(
        period="1d",
        interval="5m"
    )


    prezzo = dati["Close"]

    volume = dati["Volume"]


    vwap = (
        (prezzo * volume)
        .sum()
        /
        volume.sum()
    )


    return round(
        float(vwap),
        2
    )
