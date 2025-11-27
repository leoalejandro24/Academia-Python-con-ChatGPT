# La función (o método) split() en Python se usa para dividir un string en partes, 
# usando un separador, y devuelve una lista con los fragmentos resultantes.

# Dividir una cadena (split)

cadena = "Hola Mundo"
palabras = cadena.split() # Por defecto separa por espacios
print(palabras) # Resultado: ['Hola', 'Mundo']

cadena = "Hola Mundo"
palabras = cadena.split("M") # Separando por la palabra M
print(palabras) # Resultado: ['Hola ', 'undo']

# Buscar (find)

posicion = cadena.find("Mundo") # Buscamos la cadena Mundo, nos devuelve el indice de la posición, si no encuentra
# la palabra buscada nos devuelve -1
print(posicion) # Resultado: 5

# Reemplazar (replace)

nueva_cadena = cadena.replace("Mundo", "Amigo") # Reemplazamos la palabra Mundo por Amigo.
print(nueva_cadena) # Resultado: Hola Amigo

# Multiplicación de cadenas
cadena = "Hola "
resultado_multiplicación_de_cadena = cadena * 3 # Repetimos la cantidad de veces que queremos que salga la cadena
print(resultado_multiplicación_de_cadena) # Resultado: Hola Hola Hola

# Limpiar cadenas (strip)

cadena = "   Hola Mundo    "
cadena2 = "....Hola Mundo....."
cadena_limpia = cadena.strip() # Metodo strip nos elimina espacios en blancos del inicio y fin de una cadena,
# nos elimina saltos de linea, tabulaciones, etc..
cadena2_limpia = cadena2.strip(".") # Podemos especificar el caracter a eliminar de los inicios y finales.
print(cadena_limpia) # Resultado: Hola Mundo
print(cadena2_limpia) # Resultado: Hola Mundo