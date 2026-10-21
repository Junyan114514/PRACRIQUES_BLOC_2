import random

def menu():
     while True:
         print("\nJoc d'endevinar número")
         print("1. Jugar")
         print("2. Sortir")

         opcio = input("Selecciona una opció: ")
         if opcio == "1":
             def Jugar():
                 lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
                 Solucio = random.choice(lista)
                 while True:
                    print("Esciu un numero entre 1 i 50")
                    a = int(input("Esciu un numero: "))
                    if a == Solucio:
                     print("Correcta!")
                     break
                    elif a < Solucio:
                     print("El numero es mes gran")
                     continue
                    elif a > Solucio:
                     print("El numero es mes petit")
                     continue
             Jugar()
         elif opcio == "2":
            print("Bey bey~")
            break

menu()