from yahoo_data import (
    get_spx_price as yahoo_spx,
    get_intraday_prices as yahoo_prices,
    get_vwap as yahoo_vwap
)


def get_spx_price():

    try:
        return yahoo_spx()

    except Exception:

        return 6500



def get_intraday_prices():

    try:
        prezzi = yahoo_prices()

        if len(prezzi) > 0:
            return prezzi

    except Exception:
        pass


    # fallback demo

    return [
        6480,
        6485,
        6490,
        6498,
        6500
    ]



def get_vwap():

    try:
        return yahoo_vwap()

    except Exception:

        return 6480
