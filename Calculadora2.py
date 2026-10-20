import math

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

        opcio = input("Escriu que vol fer: ")

        if opcio == "1":
             def suma():
                 numero1 = (input("Primer número: "))
                 numero2 = (input("Segon número: "))

                 numero1 = int(numero1)
                 numero2 = int(numero2)  
                 suma = numero1 + numero2
                 print(suma)

             suma()

        elif opcio == "2":
            def Resta():
                numero1 = (input("Primer número: "))
                numero2 = (input("Segon número: "))

                numero1 = int(numero1)
                numero2 = int(numero2)
                resta = numero1 - numero2
                print(resta)

            Resta()
        elif opcio == "3":
            def Multiplicacio():
                numero1 = (input("Primer número: "))
                numero2 = (input("Segon número: "))

                numero1 = int(numero1)
                numero2 = int(numero2)
                multiplicacio = numero1 * numero2
                print(multiplicacio)

            Multiplicacio()
        elif opcio == "4":
            def Divisio():
                numero1 = (input("Primer número: "))
                numero2 = (input("Segon número: "))

                numero1 = int(numero1)
                numero2 = int(numero2)
                divisio = numero1 / numero2
                print(divisio)

            Divisio()
        elif opcio == "5":
            def equqcio_de_primer_grau():
                while True:
                    print("1. Ax + b = 0")
                    print("2. Ax + b = c")
                    print("3. Ax = b")
                    print("4. Tornar menu")

                    opcio = input("Escriu que vol fer: ")

                    if opcio == "1":
                        ax = (input("Valor de a: "))
                        b = (input("Valor de b: "))

                        ax = int(ax)
                        b = int(b)

                        Solucio = -b / ax
                        print("x =", Solucio)

                    elif opcio == "2":
                        ax = (input("valor de a : "))
                        b = (input("valor de b : "))
                        c = (input("valor de c : "))

                        ax = int(ax)
                        b = int(b)  
                        c = int(c)

                        solucio = (c - b) / ax
                        print("x =", solucio)

                    elif opcio == "3":
                        ax = (input("valor de a : "))
                        b = (input("valor de b : "))

                        ax = int(ax)
                        b = int(b)

                        solucio = b / ax
                        print("x =", solucio)

                    elif opcio == "4":
                        break
            equqcio_de_primer_grau()

        elif opcio == "6":
            def equacio_de_segona_grau():
                while True:
                    print("1. Ax2 + bx + c = 0")
                    print("2. Ax2 + bx = 0")
                    print("3. Ax2 + c = 0")
                    print("4. Tornar menu")

                    Opcio = input("Escriu que vol fer: ")

                    if Opcio == "1":             
                         a = (input("Valor de a: "))
                         b = (input("Valor de b: "))
                         c = (input("Valor de c: "))

                         a = int(a)
                         b = int(b)
                         c = int(c)
                         d = b * b - 4 * a * c
                         if d < 0:
                             print("No hi ha solucions reals.")
                         elif d == 0:
                             x = -b / (2 * a)
                             print("Una solucio:", x)
                         else:
                             x1 = (-b + math.sqrt(d)) / (2 * a)
                             x2 = (-b - math.sqrt(d)) / (2 * a)
                             print("Dues solucions:", x1, "i", x2)
                    elif Opcio == "2":
                        a=(input("valor de a:"))
                        b=(input("valor de b:"))

                        a=int(a)
                        b=int(b)

                        Solucio1=0
                        Solucio2=(-b / a)
                        print("x1 =", Solucio1)
                        print("x2 =", Solucio2)

                    elif Opcio == "3":
                        a=(input("valor de a:"))
                        c=(input("valor de c:"))

                        a=int(a)
                        c=int(c)

                        Solucio1=math.sqrt(-c / a)
                        Solucio2=-math.sqrt(-c / a)
                        print("x1 =", Solucio1)
                        print("x2 =", Solucio2)

                    elif Opcio == "4":
                        break
            equacio_de_segona_grau()
        
        elif opcio == "7":
            def Funcions():
                while True:
                    print("1. f(x) = ax + b")
                    print("2. Tornar menu")

                    opcio = input("Escriu que vol fer: ")

                    if opcio == "1":
                        a = (input("Valor de a: "))
                        b = (input("Valor de b: "))
                        x = (input("Valor de x: "))

                        a = int(a)
                        b = int(b)
                        x = int(x)

                        resultat = a * x + b
                        print("f(x) =", resultat)

                    elif opcio == "2":
                        break
            Funcions()
        elif opcio == "8":
            def Geometria():
                while True:
                    print("1. Area del rectangle")
                    print("2. Area del triangle")
                    print("3. Area del cercle")
                    print("4. Pitagoras")
                    print("5. Tornar menu")

                    opcio = input("Escriu que vol fer: ")

                    if opcio == "1":
                        base = (input("Base: "))
                        altura = (input("Altura: "))

                        base = int(base)
                        altura = int(altura)

                        area = base * altura
                        print("Area:", area)

                    elif opcio == "2":
                        base = (input("Base: "))
                        altura = (input("Altura: "))

                        base = int(base)
                        altura = int(altura)

                        area = base * altura / 2
                        print("Area:", area)

                    elif opcio == "3":
                        radi = (input("Radi: "))

                        radi = int(radi)

                        area = math.pi * radi ** 2
                        print("Area:", area)

                    elif opcio == "4":
                        while True:
                            print("1. Calcular la Hipotenusa")
                            print("2. Calcular el catet")
                            print("3. Calcular l'oposat")
                            print("4. Tornar menu")

                            opcio = input("Escriu que vol fer: ")

                            if opcio == "1":
                                catet = (input("Valor del catet 1: "))
                                oposat = (input("Valor del oposat 2: "))

                                catet = int(catet)
                                oposat = int(oposat)

                                hipotenusa = math.sqrt(catet ** 2 + oposat ** 2)
                                print("Hipotenusa:", hipotenusa)

                            elif opcio == "2":
                                hipotenusa = (input("Valor de la hipotenusa: "))
                                oposat = (input("Valor del oposat: "))

                                hipotenusa = int(hipotenusa)
                                oposat = int(oposat)

                                catet = math.sqrt(hipotenusa ** 2 - oposat ** 2)
                                print("Catet:", catet)

                            elif opcio == "3":
                                hipotenusa = (input("Valor de la hipotenusa: "))
                                catet = (input("Valor del catet: "))

                                hipotenusa = int(hipotenusa)
                                catet = int(catet)

                                oposat = math.sqrt(hipotenusa ** 2 - catet ** 2)
                                print("Oposat:", oposat)

                            elif opcio == "4":
                                break

                    elif opcio == "5":
                        break
            Geometria()
        elif opcio == "9":
            print("Sortir")
            break

menu()
