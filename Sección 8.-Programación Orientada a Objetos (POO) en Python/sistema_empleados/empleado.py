# Sistema de Empleados

# Crea un sistema de manejo de empleados de una empresa, 
# aplicando la programación orientada a objetos.

# La empresa desea saber el total de empleados así como el total de empleados de un departamento en particular.

# Se debe crear la clase de Empleado y Empresa en archivos por separado, 
# así como la creación de objetos en un archivo por separado.

class Empleado:
    contador_empleados = 0

    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        Empleado.contador_empleados += 1
        self.id = Empleado.contador_empleados

    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados
    
