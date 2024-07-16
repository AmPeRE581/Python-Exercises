#Exercise6: Calendar with Update#

import calendar
from datetime import date

def stampa_calendario(anno):
    for mese in range(1, 13):
        # Ottieni il calendario del mese specificato
        calendario = calendar.monthcalendar(anno, mese)

        # Determina il nome del mese
        nome_mese = calendar.month_name[mese]

        # Stampa l'intestazione del calendario
        print(f"Calendario di {nome_mese} {anno}")
        print("---------------------------")
        print("LUN MAR MER GIO VEN SAB DOM")

        # Stampa ogni settimana del calendario
        for settimana in calendario:
            for giorno in settimana:
                # Stampa il giorno se è diverso da zero, altrimenti stampa spazio vuoto
                if giorno == 0:
                    print("   ", end=' ')
                else:
                    # Evidenzia il giorno corrente
                    oggi = date.today()
                    if giorno == oggi.day and mese == oggi.month and anno == oggi.year:
                        print(f"\033[1;37;41m {giorno:2} \033[m", end=' ')
                    else:
                        # Verifica se il giorno è festivo
                        if calendar.weekday(anno, mese, giorno) in [5, 6] or is_festivo(anno, mese, giorno):
                            print(f"\033[1;31m {giorno:2} \033[m", end=' ')
                        else:
                            print(f"{giorno:3}", end=' ')
            print()  # Vai alla prossima riga per la nuova settimana
        print()  # Spazio tra i mesi

def is_festivo(anno, mese, giorno):
    # Esempio di verifica per festività fisse (puoi personalizzare questa funzione)
    festivita_fisse = {
        (1, 1),    # Capodanno
        (1, 6),    # Epifania
        (4, 25),   # Festa della Liberazione
        (5, 1),    # Festa del Lavoro
        (6, 2),    # Festa della Repubblica
        (8, 15),   # Assunzione di Maria
        (11, 1),   # Ognissanti
        (12, 8),   # Immacolata Concezione
        (12, 25),  # Natale
        (12, 26),  # Santo Stefano
    }
    return (mese, giorno) in festivita_fisse

anno = 2024
stampa_calendario(anno)

"""
Spiegazione delle modifiche:

- Colore dei giorni festivi: 
Utilizziamo il formato ANSI per colorare i giorni festivi. 
Il codice \033[1;31m rende il testo rosso brillante (31 è il codice per il colore rosso) 
e \033[m reimposta il colore alla normale formattazione.

- Funzione is_festivo: 
Questa funzione verifica se una data specifica è un giorno festivo. 
Nell'esempio fornito, ci sono alcune festività fisse per l'Italia. 
Puoi personalizzare questa funzione per includere o escludere altre festività a seconda delle tue necessità.

- Ciclo per un intero anno: 
Il codice è stato modificato per ciclare attraverso tutti i mesi (da gennaio a dicembre) di un dato anno, 
stampando il calendario per ciascun mese.

- Evidenziazione del giorno corrente: 
Utilizziamo il modulo datetime per ottenere la data odierna e evidenziare il giorno corrente nel calendario 
con un colore diverso (bianco su rosso). """