#Exercise8: Indovina il Numero

import random

def play_game(max_attempts, min_val, max_val):
    numero = random.randint(min_val, max_val)
    tentativi = 0
    print(f"Indovina il numero tra {min_val} e {max_val}:")

    while tentativi < max_attempts:
        try:
            guess = int(input())
            tentativi += 1

            if guess > numero:
                print("Troppo alto! Riprova:")
            elif guess < numero:
                print("Troppo basso! Riprova:")
            else:
                print(f"Esatto! Hai indovinato in {tentativi} tentativi.")
                break

            if tentativi == max_attempts:
                print(f"Hai superato il numero massimo di tentativi. Il numero era {numero}.")
        except ValueError:
            print("Inserisci un numero valido!")

def main():
    print("Benvenuto al gioco dell'Indovina Numero!")
    print("In questo gioco, devi indovinare un numero compreso in un intervallo specificato.")
    print("Puoi scegliere un livello di difficoltà o un intervallo personalizzato.")
    print("Hai un numero limitato di tentativi per indovinare il numero corretto.")
    print("Buona fortuna!")

    while True:
        print("\nSeleziona il livello di difficoltà:")
        print("1. Facile (1-50)")
        print("2. Medio (1-100)")
        print("3. Difficile (1-200)")
        print("4. Personalizzato")
        
        scelta = input()
        
        if scelta == '1':
            min_val = 1
            max_val = 50
            max_attempts = 10
        elif scelta == '2':
            min_val = 1
            max_val = 100
            max_attempts = 10
        elif scelta == '3':
            min_val = 1
            max_val = 200
            max_attempts = 15
        elif scelta == '4':
            min_val = int(input("Inserisci il valore minimo dell'intervallo: "))
            max_val = int(input("Inserisci il valore massimo dell'intervallo: "))
            max_attempts = int(input("Inserisci il numero massimo di tentativi: "))
        else:
            print("Scelta non valida. Impostato a livello Medio.")
            min_val = 1
            max_val = 100
            max_attempts = 10

        play_game(max_attempts, min_val, max_val)

        giocare_ancora = input("Vuoi giocare di nuovo? (s/n): ").strip().lower()
        if giocare_ancora != 's':
            break

if __name__ == "__main__":
    main()