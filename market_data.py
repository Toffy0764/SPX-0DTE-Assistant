def get_spx_price():
    """
    Recupera il prezzo SPX.
    Attualmente valore demo.
    Verrà collegato a IBKR API.
    """

    return 6500



def get_intraday_prices():

    """
    Serie prezzi intraday.
    Attualmente dati demo.
    In futuro:
    IBKR historical bars
    """

    return [
        6480,
        6485,
        6490,
        6498,
        6500
    ]



def get_vwap():

    """
    VWAP giornata.
    Attualmente valore demo.
    In futuro calcolo da dati reali.
    """

    return 6480 
