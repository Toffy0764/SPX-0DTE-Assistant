def controlla_evento_macro(evento):

    if evento == "alto":

        return {
            "stato": "ATTENZIONE",
            "azione": "Ridurre size o evitare trade",
            "moltiplicatore_size": 0.5
        }

    elif evento == "medio":

        return {
            "stato": "CAUTELA",
            "azione": "Operare con size ridotta",
            "moltiplicatore_size": 0.75
        }

    else:

        return {
            "stato": "NORMALE",
            "azione": "Nessuna limitazione",
            "moltiplicatore_size": 1
        }
