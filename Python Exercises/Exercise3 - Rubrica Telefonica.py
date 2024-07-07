"""

Esercizio: Rubrica Telefonica
Scrivi un programma in Python che permetta di gestire una rubrica telefonica. 
Il programma deve consentire di:

- Aggiungere un nuovo contatto.
- Visualizzare tutti i contatti.
- Cercare un contatto per nome.
- Eliminare un contatto per nome.
- Uscire dal programma.

Istruzioni:

- Crea un dizionario vuoto per memorizzare i contatti.
- Implementa un menu che consenta all'utente di scegliere tra le varie opzioni.
- Implementa le funzioni necessarie per ogni operazione (aggiungi, visualizza, cerca, elimina).
- Continua a mostrare il menu finché l'utente non sceglie di uscire.

"""

def aggiungi_contatto(rubrica):
    nome = input("Inserisci il nome del contatto: ")
    numero = input("Inserisci il numero di telefono: ")
    rubrica[nome] = numero
    print(f"Contatto {nome} aggiunto con successo.\n")

def visualizza_contatti(rubrica):
    if not rubrica:
        print("La rubrica è vuota.\n")
    else:
        print("Contatti nella rubrica:")
        for nome, numero in rubrica.items():
            print(f"Nome: {nome}, Numero: {numero}")
        print()

def cerca_contatto(rubrica):
    nome = input("Inserisci il nome del contatto da cercare: ")
    if nome in rubrica:
        print(f"Nome: {nome}, Numero: {rubrica[nome]}\n")
    else:
        print(f"Contatto {nome} non trovato.\n")

def elimina_contatto(rubrica):
    nome = input("Inserisci il nome del contatto da eliminare: ")
    if nome in rubrica:
        del rubrica[nome]
        print(f"Contatto {nome} eliminato con successo.\n")
    else:
        print(f"Contatto {nome} non trovato.\n")

def main():
    rubrica = {}
    while True:
        print("Menu:")
        print("1. Aggiungi contatto")
        print("2. Visualizza contatti")
        print("3. Cerca contatto")
        print("4. Elimina contatto")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1':
            aggiungi_contatto(rubrica)
        elif scelta == '2':
            visualizza_contatti(rubrica)
        elif scelta == '3':
            cerca_contatto(rubrica)
        elif scelta == '4':
            elimina_contatto(rubrica)
        elif scelta == '5':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.\n")

if __name__ == "__main__":
    main()
