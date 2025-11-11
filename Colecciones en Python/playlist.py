
# Aqui se define la lista

lista_reproduccion = []
numero_canciones = int(input("Cuantas canciones desea agregar: "))

# Iteramos cada elemento de la lista para agregar un nuevo elemento

for indice in range(numero_canciones):
    cancion = input(f"Proporciona la cancion {indice + 1}")
    lista_reproduccion.append(cancion)

# Empezamos a agregar canciones

# lista_reproduccion.append("Hotel California - Eagles")
# lista_reproduccion.append("Dream on - Aerosmith")
# lista_reproduccion.append("Staying Alive - Bee Gees")

# Ordenar la lista en orden alfabetico

lista_reproduccion.sort() # Con sort ordenamos la lista en orden alfabetico
#lista_reproduccion.sort(reverse=True) Con reverse=True ordenamos la lista descendente

# Mostrar la lista de canciones

print("Lista de reproducción en orden alfabetico")
for cancion in lista_reproduccion:
    print(cancion)
