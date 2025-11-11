def superheroe_superpoderes(superheroe, nombre, *args): # Al usar el * son variables que pueden ser muchas o pocas. Se crea una tupla con todos los argumentos pasados.
    print(f"Superheroe: {superheroe} - {nombre} - {args}")
    # Iteramos los superpoderes
    for superpoder in args:
        print(f"\tSuperpoder: {superpoder}")

# Llamar a la función
superheroe_superpoderes("Spiderman", "Peter Parker", "Instinto Arácnido", "Telaraña")
superheroe_superpoderes("Ironman", "Tony Stark", "Armadura", "Playboy", "Milonario") # Vemos que independiente de la cantidad de valores que damos en args nos imprime todos en una tupla

# Es opcional enviar argumentos variables
superheroe_superpoderes("Mi vecino", "Juan Perez")




