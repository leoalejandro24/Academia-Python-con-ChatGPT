# Definir una lista que almacena tuplas de productos

productos = [
    ("P001", "Camiseta", 20.00),
    ("P002", "Jeans", 30.00),
    ("P003", "Sudadera", 40.00)
]

# Imprimimos la información de cada producto y calculamos el total

print("Información de los productos")

precio_total = 0

for producto in productos:
    id, descripcion, precio = producto # Desempaquetado
    print(f"Producto: ID = {id}, Descripción = {descripcion}, Precio = {precio}")
    precio_total += precio

print(f"El precio total es de {precio_total}")
    
     