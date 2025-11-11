# kwargs - keyword arguments (key, value)

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f"Superheroe: {nombre} - {args}. Mas info: {kwargs}")

# Llamamos la función
superheroe_superpoderes("Spiderman", "Instinto Arácnido", edad=17, empresa="Marvel") # El primer parametro se asigna a nombre, el segundo que esta separado por coma se asigna a *args y los que tienen llave-valor a **kwargs
superheroe_superpoderes("Ironman", "Armadura", "Playboy", edad=45)

# Es opcional enviar argumentos variables
superheroe_superpoderes("Mi vecino", personalidad="Buena onda!")