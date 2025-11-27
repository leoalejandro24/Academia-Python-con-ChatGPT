# Sintaxis: sorted(iterable, key=None, reverse=False)

empleado = ["Juan", "Pedro", "Maria"]

# Ordenamos la lista

empleados_ordenados = sorted(empleado) # Ordena de forma ascendente de forma predeterminada

print(empleados_ordenados) # Resultado: ['Juan', 'Maria', 'Pedro']

empleados_ordenados_desc = sorted(empleado, reverse=True) # Ordenamos de forma descendente

print(empleados_ordenados_desc) # Resultado: ['Pedro', 'Maria', 'Juan']

# Ordenar un diccionario

empleados_dict = [
    {"nombre": "Juan", "Salario": 3000},
    {"nombre": "Maria", "Salario": 2500},
    {"nombre": "Pedro", "Salario": 3500}
]

empleados_ordenados_por_salario = sorted(empleados_dict, key=lambda x: x["Salario"])

print(empleados_ordenados_por_salario)