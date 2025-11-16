from sistema_empleados.empresa import Empresa
from sistema_empleados.empleado import Empleado

# Crear una instancia de una empresa
empresa1 = Empresa("Mi Empresa")

# Contratar empleados 

empresa1.contratar_empleado("Juan", "Ventas")
empresa1.contratar_empleado("Maria", "Marketing")
empresa1.contratar_empleado("Pedro", "Ventas")
empresa1.contratar_empleado("Ana", "RRHH")

# Obtener numero total de empleados
print(f"Total de empleados en la empresa: {Empleado.obtener_total_empleados()}")

# Obtener el numero de empleados en el departamento de ventas
print(f"Empleados en el departamento de ventas: {empresa1.obtener_numero_empleados_departamento("Ventas")}")

# Mostrar todos los empleados de la empresa
empresa1.mostrar_todos_los_empleados()

