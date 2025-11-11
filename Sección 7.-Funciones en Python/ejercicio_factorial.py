# Realizado por mi
def factor(numero):
    factorial = 1
    if numero == 1:
        print(f"El factorial de {numero} = {factorial}")
    elif numero > 1:
        for n in range(2, numero):
            factorial = n*factorial
        print(f"El factorial de {numero} es = {numero*factorial}")
        factor(numero-1)

# Respuesta
def factorial_recursivo(numero):
    # Caso base: factorial de 0 o 1 es 1
    if numero == 0 or numero == 1:
        return 1
    # Caso recursivo, calcular factorial del numero reducido en 1
    else:
        return numero * factorial_recursivo(numero - 1)
