from functools import reduce


numeros = [1,2,3,4,5]

# reduce y map

suma_acumulativa = reduce(lambda x, y: x + y, numeros)

print(suma_acumulativa)