
import math

def suma():
    a = float(input("Primer numero: "))
    b = float(input("Segon numero: "))
    print("Resultat:", a + b)


def resta():
    a = float(input("Primer numero: "))
    b = float(input("Segon numero: "))
    print("Resultat:", a - b)


def multiplicacio():
    a = float(input("Primer numero: "))
    b = float(input("Segon numero: "))
    print("Resultat:", a * b)


def divisio():
    a = float(input("Primer numero: "))
    b = float(input("Segon numero: "))
    if b != 0:
        print("Resultat:", a / b)
    else:
        print("Error: No es pot dividir per zero.")

def equacio_primer_grau():
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))

    if a != 0:
        x = -b / a
        print("La solucio es:", x)
    elif b == 0:
        print("Infinites solucions.")
    else:
        print("No te solucio.")


def equacio_segon_grau():
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))

    if a == 0:
        print("No es una equacio de segon grau.")
    else:
        d = b * b - 4 * a * c

        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print("Dues solucions:", x1, "i", x2)
        elif d == 0:
            x = -b / (2 * a)
            print("Una solucio:", x)
        else:
            print("No hi ha solucions.")


def funcio():
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    x = float(input("Valor de x: "))

    resultat = a * x + b
    print("f(x) =", resultat)


def geometria():
    while True:
        print("\nGEOMETRIA")
        print("1. Area del rectangle")
        print("2. Area del triangle")
        print("3. Area del cercle")
        print("4. Tornar al menu")

        opcio = input("Tria una opcio: ")

        if opcio == "1":
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            print("Area:", base * altura)

        elif opcio == "2":
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            print("Area:", base * altura / 2)

        elif opcio == "3":
            radi = float(input("Radi: "))
            print("Area:", math.pi * radi ** 2)

        elif opcio == "4":
            break

        else:
            print("Opcio incorrecta.")


def menu():
    while True:
        print("\nCALCULADORA")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacio")
        print("4. Divisio")
        print("5. Equacio de primer grau")
        print("6. Equacio de segon grau")
        print("7. Funcions")
        print("8. Geometria")
        print("9. Sortir")

        opcio = input("Introdueix una opcio: ")

        if opcio == "1":
            suma()
        elif opcio == "2":
            resta()
        elif opcio == "3":
            multiplicacio()
        elif opcio == "4":
            divisio()
        elif opcio == "5":
            equacio_primer_grau()
        elif opcio == "6":
            equacio_segon_grau()
        elif opcio == "7":
            funcio()
        elif opcio == "8":
            geometria()
        elif opcio == "9":
            print("Adeu!")
            break
        else:
            print("Opcio incorrecta. Torna-ho a provar.")


menu()