agenda = {
    "Carlos": {
        "telefono": "556677711",
        "email": "carlos@mail.com",
        "dirección": "Calle Principal 132"
    },
    "María": {
        "telefono": "99887733",
        "email": "maria@mail.com",
        "dirección": "Avenida Central 456"
    },
    "Pedro": {
        "telefono": "55139078",
        "email": "pedro@mail.com",
        "dirección": "Plaza Mayor 789"
    }
}

print(agenda)

# Acceder a la información de un contacto en especifico

print(f"""Información del contacto de María
    Telefono: {agenda["María"]["telefono"]}
    Email: {agenda["María"]["email"]}
    Dirección: {agenda["María"]["dirección"]}""")

# Agregar un nuevo contacto

agenda["Ana"] = {
    "telefono": "55678392",
    "email": "ana@mail.com",
    "dirección": "Calle Salvador Diaz 321"
}

print(agenda)

# Eliminar un contacto existente

# del agenda["Pedro"]

# Podemos utilizar el metodo pop

agenda.pop("Pedro")

print(agenda)

# Mostrar todos los contacto de la agenda
print("\n Lista de contactos en la agenda:")
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
          Telefono: {detalles["telefono"]}
          Email: {detalles["email"]}
          Dirección: {detalles["dirección"]}''')
