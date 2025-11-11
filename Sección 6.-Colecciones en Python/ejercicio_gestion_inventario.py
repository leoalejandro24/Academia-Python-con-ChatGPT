productos = []

cantidad_productos = int(input("Cantos productos deseas agregar al inventario?: "))

for indice in range(cantidad_productos):
    print(f"Proporciona los valores del producto {indice + 1}: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    producto_diccionario = {"id": indice, "nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto_diccionario)

print(productos)

id_a_buscar = int(input("Ingresa el ID del producto que desea buscar: "))

print(f"""Información del producto encontrado:
      ID: {productos[id_a_buscar]["id"]}
      Nombre: {productos[id_a_buscar]["nombre"]}
      Precio: {productos[id_a_buscar]["precio"]}
      Cantidad: {productos[id_a_buscar]["cantidad"]}""")

print("Inventario actualizado: \n")

for producto in productos:
    print(f"""ID: {producto["id"]}
Nombre: {producto["nombre"]}
Precio: {producto["precio"]}
Cantidad: {producto["cantidad"]}""")
    
