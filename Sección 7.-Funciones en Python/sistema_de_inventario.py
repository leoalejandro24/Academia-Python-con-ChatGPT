print("*** Sistema de Inventarios ***")

productos = [{"ID":1, "nombre": "Camisa", "Precio": 25.99, "Cantidad": 50},
             {"ID":2, "nombre": "Pantalones", "Precio": 39.99, "Cantidad": 30},
             {"ID":3, "nombre": "Zapatos", "Precio": 49.99, "Cantidad": 20}]

def menu():
    print(
        """Menú
            1.- Mostrar inventario
            2.- Agregar nuevo producto
            3.- Buscar producto por ID
            4.- Salir""")
    opción = int(input("Seleccione una opción: "))
    if opción == 1:
        mostrar_inventario()
    elif opción == 2:
        agregar_producto()
    elif opción == 3:
        buscar_por_id()
    elif opción == 4:
        salir()
    else:
        print("Propociona una opción valida")
        menu()

def mostrar_inventario():
    print("Inventario del almácen: ")
    for producto in productos:
        print(f"ID: {producto["ID"]}, Nombre: {producto["nombre"]}, Precio: {producto["Precio"]}, Cantidad: {producto["Cantidad"]}")
    menu()

def agregar_producto():
    print("--- Agregar Nuevo Producto ---")
    id = int(input("ID: "))
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    nuevo_producto = {"ID": id, "nombre": nombre, "Precio": precio, "Cantidad": cantidad}
    productos.append(nuevo_producto)
    print("Producto agregado al inventario.")
    menu()

def buscar_por_id():
    print("--- Buscar Producto por ID ---")
    buscar = int(input("Ingrese el ID del producto que desea buscar: ")) - 1
    indices = []
    for indice, producto2 in enumerate(productos):
        indices.append(indice)
    if buscar in indices:
        print(f"ID: {productos[buscar]["ID"]}, Nombre: {productos[buscar]["nombre"]}, Precio: {productos[buscar]["Precio"]}, Cantidad: {productos[buscar]["Cantidad"]}")
    else:
        print("Producto no encontrado.")
    menu()

def salir():
    print("Hasta luego.")

if __name__ == "__main__":
    menu()

