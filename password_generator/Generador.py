import random
import string

longitud = int(input("¿Longitud de la contraseña?"))

caracteres = string.ascii_lowercase #abcdefghijklmnopqrstuvwxyz
mayusculas = input("¿Incluir mayúsculas? (si/no): ")
if mayusculas == "si":
    caracteres += string.ascii_uppercase

numeros = input("¿Incluir números? (si/no): ")
if numeros == "si":
    caracteres += string.digits

simbolos = input("¿Incluir símbolos? (si/no): ")
if simbolos == "si":
    caracteres += string.punctuation

contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)

print(contraseña)
