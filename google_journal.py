import requests


GOOGLE_SHEET_URL = https://script.google.com/macros/s/AKfycbwxQk_PWdpbB9s39r18kdVE4YJDIpHmSPXy4vZpW9u8eXV8NxiAWL5wNvIMLcmty3mq/exec


def salva_su_google_sheet(dati):

    try:

        response = requests.post(
            GOOGLE_SHEET_URL,
            json=dati,
            timeout=10
        )

        return response.text == "OK"


    except Exception as e:

        print(
            "Errore Google Journal:",
            e
        )

        return False
