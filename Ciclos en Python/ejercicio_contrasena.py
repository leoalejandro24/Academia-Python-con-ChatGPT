salir = True
contraseña = "leoa123"

while salir:
    entrada = input("Ingrese la contraseña: ")
    if entrada != contraseña:
        print("Contraseña incorrecta...")
    else:
        print("Bienvenido.")
        salir = False