terminamos = 0
def funcionSuma ():
 numero1 = input ("Primer número: ")
 numero2 = input("Segundo número: ")

 numero1 = int ( numero1)
 numero2 = int ( numero2)

 suma = numero1 + numero2
 print ( suma)
while terminamos == 0:
 print ( "Nuestras opciones:")
 print ( "1. Realizar una suma")
 print ( "2. Terminar")

 pregunta = input ( "¿Qué quieres hacer? (1 o 2): ")

 if pregunta == "1":
  funcionSuma ()
 elif pregunta == "2":
  print ( "Adiós")
 terminamos = 1