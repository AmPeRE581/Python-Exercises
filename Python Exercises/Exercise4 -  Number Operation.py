"""

Exercise4: Permette di memorizzare 5 numeri, scambiarli, 
stamparli e poi selezionare un numero da ripetere due volte:

"""

# Funzione per memorizzare 5 numeri
def memorizza_numeri():
    numeri = []
    print("Inserisci 5 numeri:")
    for i in range(5):
        numero = int(input(f"Numero {i+1}: "))
        numeri.append(numero)
    return numeri

# Funzione per scambiare due numeri nella lista
def scambia_numeri(numeri):
    print("\nStato attuale della lista:", numeri)
    index1 = int(input("Inserisci l'indice del primo numero da scambiare (0-4): "))
    index2 = int(input("Inserisci l'indice del secondo numero da scambiare (0-4): "))
    numeri[index1], numeri[index2] = numeri[index2], numeri[index1]
    return numeri

# Funzione per ripetere un numero due volte
def ripeti_numero(numeri):
    numero_da_ripetere = int(input("\nInserisci il numero da ripetere due volte: "))
    if numero_da_ripetere in numeri:
        numeri.remove(numero_da_ripetere)
        numeri.append(numero_da_ripetere)
        numeri.append(numero_da_ripetere)
    else:
        print("Il numero inserito non è presente nella lista.")
    return numeri

# Programma principale
def main():
    numeri = memorizza_numeri()
    print("\nLista originale:", numeri)
    
    numeri = scambia_numeri(numeri)
    print("Lista dopo lo scambio:", numeri)
    
    numeri = ripeti_numero(numeri)
    print("Lista dopo aver ripetuto il numero:", numeri)

# Avvio del programma
if __name__ == "__main__":
    main()
