print("*** Cajero Automatico ***")

saldo = 1000
salir = True

while salir:
    print('''Operaciones que puede realizar:
            1.- Consultar Saldo
            2.- Retirar
            3.- Depositar
            4.- Salir''')
    
    opcion = int(input("Ingresa una opción: "))

    if opcion == 1:
        print(f"Su saldo actual es {saldo}")

    if opcion == 2:
        retiro = int(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print(f"Saldo insuficiente, su saldo es de {saldo}")
        else:
            saldo -= retiro
            print(f"Su nuevo saldo es de {saldo}")
    if opcion == 3:
        ingreso = int(input("Ingrese la cantidad a depositar: "))
        saldo += ingreso
        print(f"Su nuevo saldo es de {saldo}")

    if opcion == 4:
        print("Saliendo del sistema...")
        salir = False
