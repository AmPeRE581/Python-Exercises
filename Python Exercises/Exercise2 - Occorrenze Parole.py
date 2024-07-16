#Exercise2: Occorrenze Parole#

import re
from collections import Counter

def conta_occorrenze_parole(testo):
    # Converti il testo in minuscolo
    testo = testo.lower()
    
    # Rimuovi la punteggiatura utilizzando le espressioni regolari
    testo = re.sub(r'[^\w\s]', '', testo)
    
    # Dividi il testo in una lista di parole
    parole = testo.split()
    
    # Conta le occorrenze di ciascuna parola
    contatore = Counter(parole)
    
    # Stampa ogni parola con il relativo conteggio
    for parola, conteggio in contatore.items():
        print(f"{parola}: {conteggio}")

# Chiedi all'utente di inserire una stringa di testo
testo_utente = input("Inserisci una stringa di testo: ")

# Chiama la funzione per contare le occorrenze delle parole
conta_occorrenze_parole(testo_utente)

#Spiegazione del codice:
#Importazione dei moduli: Vengono importati i moduli re per le espressioni regolari e Counter dalla libreria collections per contare le parole.
#Conversione in minuscolo: La stringa di testo viene convertita in minuscolo usando il metodo lower() per ignorare la distinzione tra maiuscole e minuscole.
#Rimozione della punteggiatura: Viene utilizzata l'espressione regolare re.sub(r'[^\w\s]', '', testo) per rimuovere tutti i caratteri che non sono parole o spazi.
#Divisione in parole: Il testo viene diviso in una lista di parole usando il metodo split().
#Conteggio delle parole: Utilizziamo Counter(parole) per contare le occorrenze di ciascuna parola nella lista.
#Stampa dei risultati: Un ciclo for stampa ogni parola con il relativo conteggio.
#Questo programma permette all'utente di inserire una stringa di testo e visualizza quante volte ciascuna parola appare nella stringa, ignorando la punteggiatura e le differenze tra maiuscole e minuscole.