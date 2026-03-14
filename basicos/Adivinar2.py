import random

opciones = ["piedra", "papel", "tijera"]

while True:
    computadora = random.choice(opciones)
    usuario = input("piedra, papel o tijera: ")
    if usuario == computadora:
        print("Empate")
    elif usuario == "piedra" and computadora == "tijera":
        print("Ganas")
    elif usuario == "papel" and computadora == "piedra":
        print("Ganas")
    elif usuario == "tijera" and computadora == "papel":
        print("Ganas")
    else:
        print("Pierdes")
    repetir = input ("¿Quieres jugar otra vez? (si/no): ")
    if repetir != "si":
        break
