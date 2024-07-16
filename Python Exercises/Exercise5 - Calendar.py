#Exercise5: Svolgimento di un semplice calendario...

import calendar

def stampa_calendario(anno, mese):
    # Ottieni il calendario del mese specificato
    calendario = calendar.monthcalendar(anno, mese)

    # Determina il nome del mese e dell'anno
    nome_mese = calendar.month_name[mese]
    nome_anno = anno

    # Stampa l'intestazione del calendario
    print(f"Calendario di {nome_mese} {nome_anno}")
    print("---------------------------")
    print("LUN MAR MER GIO VEN SAB DOM")

    # Stampa ogni settimana del calendario
    for settimana in calendario:
        for giorno in settimana:
            # Stampa il giorno se è diverso da zero, altrimenti stampa spazio vuoto
            if giorno == 0:
                print("   ", end=' ')
            else:
                print(f"{giorno:3}", end=' ')
        print()  # Vai alla prossima riga per la nuova settimana

anno = 2024
mese = 7
stampa_calendario(anno, mese)

