# Filtrar solo los numeros pares y generar una nueva lista con estos valores

numeros = range(1, 10+1) # Una lista desde el 1 al 10

# Sin usar comprensión de listas

numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    
print(f"Numeros pares del 1 al 10: {numeros_pares}")

# Usamos comprensión de listas
# Sintaxis: nueva_lista = [expresión for elemento in iterable if condición]

numeros_pares = [numero for numero in numeros if numero % 2 == 0]

print(f"Numeros pares del 1 al 10: {numeros_pares}")