while True:
 print("Opción 1- comenzar programa")
 print("Opción 2- imprimir listado")
 print("Opción 3- finalizar programa")
 opcion=int(input("Opción elegida: "))
 if opcion==1:
  print("¡Comenzamos!")
 elif opcion==2:
  print("Listado")
  print("Antonio, Vilafranca, Nou, septiembre")
 elif opcion==3:
  print("Hasta la próxima")
  break
 else:
  print("Opción incorrecta, debes de escribir 1, 2 o 3")

frase=input("Frase a analizar: ")
l=input("Letra para buscar su posición: ")
i=0
while i!=len(frase):
 if l!=frase[i]:
  print("No se encontró en la posición", i)
  i+=1
  continue
 print("Se encontró en la posición", i)
 break
