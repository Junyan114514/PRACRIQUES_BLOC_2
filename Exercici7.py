cadenaejemplo = "hola NouVilafranquins..."
print(cadenaejemplo.capitalize())

cadenaejemplo = "hola NouVilafranquins..."
print(cadenaejemplo.upper())

cadenaejemplo = "HOLA NOUVILAFRANQUINS..."
print(cadenaejemplo.lower())

cadenaejemplo = "Hola NouVilafranquins..."
print(len(cadenaejemplo))

cadenaejemplo = "Hola NouVilafranquins"
print(cadenaejemplo.isalnum())
cadenaejemplo = "1234567890"
print(cadenaejemplo.isalnum())
cadenaejemplo = "abcdefg1234567890"
print(cadenaejemplo.isalnum())
cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isalnum())

cadenaejemplo = " HolaNouVilafranquins"
print(cadenaejemplo.isalpha())
cadenaejemplo = "Hola NouVilafranquins"
print(cadenaejemplo.isalpha())
cadenaejemplo = "1234567890"
print(cadenaejemplo.isalpha())
cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isalpha())

cadenaejemplo = "Hola NouVilafranquins"
print(cadenaejemplo.isdigit())
cadenaejemplo = "1234567890"
print(cadenaejemplo.isdigit())
cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isdigit())

cadenaejemplo = "Hola NouVilafranquins"
print(cadenaejemplo.islower())
cadenaejemplo = "HOLA NOUVILAFRANQUINS..."
print(cadenaejemplo.islower())

cadenaejemplo = "Hola NouVilafranquins"
print(cadenaejemplo.isupper())
cadenaejemplo = "HOLA NOUVILAFRANQUINS..."
print(cadenaejemplo.isupper())

cadenaejemplo = " Hola NouVilafranquins"
print(cadenaejemplo.lstrip())
cadenaejemplo = "Hola NouVilafranquins "
print(cadenaejemplo.rstrip())
cadenaejemplo = " Hola NouVilafranquins "
print(cadenaejemplo.strip())

cadenaejemplo = "abcdefghijklmnopqrstuvwxyz"
print(max(cadenaejemplo))
print(min(cadenaejemplo))

cadenaejemplo = "AEIOU"
print(cadenaejemplo.replace('A','E'))

cadenaejemplo = "Hola NouVilafranquins..."
print(cadenaejemplo.swapcase())

cadenaejemplo = "Hola NouVilafranquins..."
print(cadenaejemplo.split())

cadenaejemplo = "01/09/2022"
print(cadenaejemplo.split("/"))