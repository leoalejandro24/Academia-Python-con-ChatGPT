# Definimos el set inicial

# suscriptores = {} Aqui se define un diccionario en vez de un set

suscriptores = set() # Creamos un set vacio en memoria

numero_suscriptores = int(input("Proporciona el numero de suscriptores iniciales : "))

for _ in range(numero_suscriptores):
    suscriptores.add((input("Nuevo suscriptor (email): ")))

print(f"Lista de suscriptores inicial: {suscriptores}")

# Verificar si un nuevo suscriptor esta en la lista

nuevo_suscriptor = input("Proporciona el nuevo suscriptor: ")

if nuevo_suscriptor in suscriptores:
    print(f"El nuevo suscriptor ya esta en la lista {nuevo_suscriptor}")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"El nuevo suscriptor se ha agregado a la lista")

# Eliminar un suscriptor existente

suscriptor_eliminar = input("Proporciona el suscriptor a eliminar: ")
if suscriptor_eliminar not in suscriptores:
    print("No existe el suscriptor")
else:
    suscriptores.remove(suscriptor_eliminar)
    print(f"El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista")

# Verificar la cantidad total de suscriptores

print(f"Cantidad total de suscriptores: {len(suscriptores)}")

# Mostrar todos los suscriptores

print(f"Lista de suscriptores")

for suscriptor in suscriptores:
    print(f"- {suscriptor}")