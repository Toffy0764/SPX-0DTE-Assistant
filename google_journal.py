import requests


GOOGLE_SHEET_URL = "INSERISCI_QUI_IL_TUO_URL"


def salva_su_google_sheet(dati):

    try:

        response = requests.post(
            GOOGLE_SHEET_URL,
            json=dati,
            timeout=10
        )

        if response.text == "OK":
            return True

        return False


    except Exception as e:

        print(
            "Errore Google Journal:",
            e
        )

        return False
