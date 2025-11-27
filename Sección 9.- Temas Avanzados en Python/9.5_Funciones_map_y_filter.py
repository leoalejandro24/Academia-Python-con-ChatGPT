# Map

numeros = [1,2,3,4,5]

# Aplicar una función lambda para obtener el cuadrado de cada número

cuadrados = list(map(lambda x: x ** 2, numeros)) # map recibe dos parametros, la función lambda y los elementos
# a iterar en este caso la lista de numeros.

print(cuadrados) # Resultado: [1, 4, 9, 16, 25]

# Filter

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)
