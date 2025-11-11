def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z # Python crea automaticamente una tupla al tener valores separados por coma

# Llamar la función

resultado = obtener_coordenadas()
print(resultado)

# Unpacking de la tupla

x, y, z = resultado

# Imprimir los valores de manera individual

print(f"Coordenada x = {x}, Coordenada y = {y}, Coordenada z = {z}")