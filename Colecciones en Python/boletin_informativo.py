suscriptores = {"luisa@mail.com", "marcos@mail.com", "elena@mail.com"}

# Verificar si un nuevo suscriptor esta en la lista

nuevo_suscriptor = "marcos@mail.com"

if nuevo_suscriptor in suscriptores:
    print(f"El nuevo suscriptor ya esta en la lista {nuevo_suscriptor}")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"El nuevo suscriptor se ha agregado a la lista")

# Eliminar un suscriptor existente

suscriptor_eliminar = "elena@mail.com"
suscriptores.remove(suscriptor_eliminar)

print(f"El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista")

# Verificar la cantidad total de suscriptores

print(f"Cantidad total de suscriptores: {len(suscriptores)}")

# Mostrar todos los suscriptores

print(f"Lista de suscriptores")

for suscriptor in suscriptores:
    print(f"- {suscriptor}")