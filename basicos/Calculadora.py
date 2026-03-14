print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicación")
print ("4. División")
operación = input("Seleccione una operación: ")
numero = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))

def sumar (a,b): 
    return a + b

def restar (a,b): 
    return a - b

def multiplicar (a,b): 
    return a * b

def dividir (a,b): 
    return a / b

if operación == "1":
    #Ejecutar Suma
    suma =  sumar(numero, numero2)
    print("La suma de", numero, "y", numero2, "es", suma)
elif operación == "2":
    #Ejecutar Resta
    resta = restar(numero, numero2)
    print("La resta de", numero, "y", numero2, "es", resta)
elif operación == "3":
    #Ejecutar Multiplicación
    multiplicación = multiplicar(numero, numero2)
    print("La multiplicación de", numero, "y", numero2, "es", multiplicación)
elif operación == "4":
    #Ejecutar División
    if numero2 == 0:
        print("No se puede dividir por cero")
    else:
        división = dividir(numero, numero2)
        print("La división de", numero, "y", numero2, "es", división)
else:
    print("Operación no válida")

print("Fin del programa")