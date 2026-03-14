import json

contactos = []

try:
    with open("contactos.json", "r") as f:
        contactos = json.load(f)
except:
    contactos = []

while True:
    print("1. Ver contactos")
    print("2. Agregar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print(contactos)
    elif opcion == 2:
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el telefono: ")
        email = input("Ingrese el email: ")
        contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
        with open("contactos.json", "w") as f:
            json.dump(contactos, f)
    elif opcion == 3:
        nombre = input("Ingrese el nombre: ")
        for contacto in contactos:
            if contacto["nombre"] == nombre:
                print(contacto)
    elif opcion == 4:
        nombre = input("Ingrese el nombre: ")
        for contacto in contactos:
            if contacto["nombre"] == nombre:
                contactos.remove(contacto)
        with open("contactos.json", "w") as f:
            json.dump(contactos, f)
    elif opcion == 5:
        break

with open("contactos.json", "w") as f:
    json.dump(contactos, f) 