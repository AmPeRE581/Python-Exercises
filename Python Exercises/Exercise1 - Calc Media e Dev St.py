#Esercizio: Calcolo della Media e della Deviazione Standard
#Scrivi un programma in Python che faccia quanto segue:

#Chieda all'utente di inserire una lista di numeri separati da spazi.
#Calcoli la media dei numeri inseriti.
#Calcoli la deviazione standard dei numeri inseriti.
#Visualizzi la media e la deviazione standard.

import math

def calcola_media(numeri):
    return sum(numeri) / len(numeri)

def calcola_dev_standard(numeri, media):
    varianza = sum((x - media) ** 2 for x in numeri) / len(numeri)
    return math.sqrt(varianza)

def main():
    numeri_input = input("Inserisci una lista di numeri separati da spazi: ")
    numeri = list(map(float, numeri_input.split()))

    if len(numeri) == 0:
        print("Devi inserire almeno un numero.")
        return

    media = calcola_media(numeri)
    dev_standard = calcola_dev_standard(numeri, media)

    print(f"La media dei numeri è: {media:.2f}")
    print(f"La deviazione standard dei numeri è: {dev_standard:.2f}")

if __name__ == "__main__":
    main()
