from random import randint

numero_jugador = 0
intentos = 0
numero_aleatorio = randint(1,50)
salir = numero_jugador == numero_aleatorio
intentos_maximos = 5


while not salir:
    numero_jugador = int(input("Ingresa un número: "))
    if numero_jugador < numero_aleatorio:
        print("El número aleatorio es mayor.", sep= " ")
        intentos +=1
        intentos_maximos -= 1
        print(f"Le quedan {intentos_maximos} intentos")
    elif numero_jugador > numero_aleatorio:
        print("El número aleatorio es menor.", sep= " ")
        intentos +=1
        intentos_maximos -= 1
        print(f"Le quedan {intentos_maximos} intentos")
    else:
        print(f"Acerto. Sus intentos fueron {intentos}")
    if intentos_maximos == 0:
        print(f"Sus intentos se acabaron. Son un total de {intentos}")


    