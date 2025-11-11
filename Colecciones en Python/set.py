# Crear un conjunto 

set = {1,2,3,4,5,4}

print(set) # Salida {1, 2, 3, 4, 5}. El valor del segundo 4 no se repite

# Agregar elementos al set

set.add(6)
set.add(7)
print(set)

# Eliminar elementos del set

set.remove(4) # Del set eliminamos el valor 4.

print(set)

# Iterar los elementos del set

for elemento in set:
    print(elemento, end=" ")

# Comprobar si existe un elemento en el set

print(2 in set) # Buscamos el valor de 2 en el set, nos devuelve un booleano (True o False)

# Esta operación la podemos realizar en sets, tuplas, listas.





