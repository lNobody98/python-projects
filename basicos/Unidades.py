def km_a_millas(km):
    return km * 0.621371

def millas_a_km(millas):
    return millas * 1.60934

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

print("1. Kilometros a millas")
print("2. Millas a kilometros")
print("3. Celsius a Fahrenheit")
print("4. Fahrenheit a Celsius")

opcion = int(input("Selecciona una opcion: "))

if opcion == 1:
    valor = float(input("Introduce los kilometros: "))
    print("Las millas son: ", km_a_millas(valor))
elif opcion == 2:
    valor = float(input("Introduce las millas: "))
    print("Los kilometros son: ", millas_a_km(valor))
elif opcion == 3:
    valor = float(input("Introduce los grados Celsius: "))
    print("Los grados Fahrenheit son: ", celsius_a_fahrenheit(valor))
elif opcion == 4:
    valor = float(input("Introduce los grados Fahrenheit: "))
    print("Los grados Celsius son: ", fahrenheit_a_celsius(valor))
else:
    print("Opcion no valida")
