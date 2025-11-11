personas = [
    {
        "nombre": "Regina",
        "apellido": "Flores",
        "edad": 21
    },
    {
        "nombre": "Alejandro",
        "apellido": "Reyes",
        "edad": 32
    }
]

print(personas)

# Acceder a un diccionario

print(f'''Nombre: {personas[0].get("nombre")}
Apellido: {personas[0].get("apellido")}
Edad: {personas[0].get("edad")}''') # Metodo get, podemos obtener el valor igualmente, indicando la clave

# Recorrer los elementos de la lista

for contador, persona in enumerate(personas): # Enumarete devuelve un indice
    print(f"""Persona {contador + 1}:
          {persona.get("nombre")}, {persona.get("apellido")}, {persona.get("edad")}""")
