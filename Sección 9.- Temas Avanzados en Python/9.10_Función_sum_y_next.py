# Función suma

lista = [1,2,3,4,5]

# Suma de todos los elementos

resultado = sum(lista)

print(resultado) # Resultado: 15

# Podemos proporcionar un valor inicial

resultado = sum(lista, 20) # Podemos añadir un valor inicial

print(resultado) # Resultado: 35

# Función next

iterador = iter(lista)

# Obtenemos el proximo elemento del iterador

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
