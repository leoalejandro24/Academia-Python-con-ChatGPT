def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1


# Creamos un generador 

var_generador = generador(5)

# Iteramos sobre el generador 

for valor in var_generador:
    print(valor)

# Expresiones generadoras

generador = (x ** 2 for x in range(10) if x % 2 == 0)

for cuadarado_pares in generador:
    print(cuadarado_pares)