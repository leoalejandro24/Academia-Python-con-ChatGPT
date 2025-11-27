nombres = ["Juan", "Maria", "Pedro"]
edades = [30, 25, 35]
ciudades = ["Madrid", "Barcelona", "Sevilla"]

# Combinar los elementos correspondientes usando la función zip

personas = zip(nombres, edades, ciudades)

# Iterar sobre el resultado de la función zip
for persona in personas:
    print(persona)