estacion = int(input("Ingrese el número de estación (1-12): "))

if estacion in [12, 1, 2]:
    print("Invierno")

elif estacion in [3, 4, 5]:
    print("Primavera")

elif estacion in [6, 7, 8]:
    print("Verano")

elif estacion in [9, 10, 11]:
    print("Otoño")
else:
    print("Número de estación inválido. Por favor ingrese un número entre 1 y 12.")

