import random

numero_secreto = random.randint(1, 20)
intentos = 0

while True:
    intento = int(input("Adivina el numero (1-20): "))
    intentos = intentos + 1
    if intento < numero_secreto:
        print("¡Muy bajo! Intenta con uno más alto")
    elif intento > numero_secreto:
        print("¡Muy alto! Intenta con uno más bajo")
    elif intento == numero_secreto:
        print("¡Correcto! Adivinaste en", intentos, "intentos")
        break
