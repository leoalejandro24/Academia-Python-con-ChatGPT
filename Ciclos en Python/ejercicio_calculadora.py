salir = True

while salir:
    print("""Operaciones que puedes realizar:
        1.- Suma
        2.- Resta
        3.- Multiplcacion
        4.- División
        5.- Salir""")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        numero1 = int(input("Ingrese el primer valor: "))
        numero2 = int(input("Ingrese el segundo valor: "))
        print(f"El resultado de la suma es: {numero1 + numero2}")
    if opcion == 2:
        numero1 = int(input("Ingrese el primer valor: "))
        numero2 = int(input("Ingrese el segundo valor: "))
        print(f"El resultado de la resta es: {numero1 - numero2}")
    if opcion == 3:
        numero1 = int(input("Ingrese el primer valor: "))
        numero2 = int(input("Ingrese el segundo valor: "))
        print(f"El resultado de la multiplicación es: {numero1 * numero2}")
    if opcion == 4:
        numero1 = int(input("Ingrese el primer valor: "))
        numero2 = int(input("Ingrese el segundo valor: "))
        print(f"El resultado de la división es: {numero1 / numero2}")
    if opcion == 5:
        print("Saliendo de la aplicación..")
        salir = False
        