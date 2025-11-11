from modulo_funcion_sumar import sumar

# arg1, arg2 = 5, 7
arg1 = int(input("Ingresa el número 1: "))
arg2 = int(input("Ingresa el número 2: "))

resultado_suma = sumar(arg1, arg2)

print(f"El resultado de la suma de {arg1} + {arg2} es: {resultado_suma}")