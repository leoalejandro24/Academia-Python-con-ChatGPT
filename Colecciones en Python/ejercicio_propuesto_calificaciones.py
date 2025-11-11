calificaciones = []
cantidad_calificaciones = int(input("¿Cuántas calificaciones deseas agregar? "))

for x in range(cantidad_calificaciones):
    calificacion = int(input(f"Calificación[{x+1}] = "))
    calificaciones.append(calificacion)

# contador = 0

# for cal in calificaciones:
#     contador += cal

# En vez de iterar uno por uno los valores de la lista, podemos usar la función sum que solicita un iterable

contador = sum(calificaciones)

print(f"Promedio de las Calificaciones: {contador/cantidad_calificaciones}")