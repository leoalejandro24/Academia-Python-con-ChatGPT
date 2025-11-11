# Es crear condiciones en una sola línea utilizando el operador ternario.

# Sintaxis: valor_si_verdadero if condicion else valor_si_falso

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Usando el operador ternario para determinar el número mayor
mayor = numero1 if numero1 > numero2 else numero2
print(f"El número mayor es: {mayor}")
